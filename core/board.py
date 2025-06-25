import numpy as np
from bitboard import bb
from Piece import Piece
from constants import HEIGHT, WIDTH, H, V, MAIN_LABEL
from Solution import Move
import copy

class EnumBoard:
    def __init__(self, mask_horizontal = bb(0), mask_vertical = bb(0)):
        self.mask_horizontal = mask_horizontal
        self.mask_vertical = mask_vertical

    def __eq__(self, other):
        return isinstance(other, EnumBoard) and self.mask_horizontal == other.mask_horizontal and self.mask_vertical == other.mask_vertical

    def __hash__(self):
        return hash((self.mask_horizontal, self.mask_vertical))

class Board:
    def __init__(self, char_board = None):
        '''
        Input:
            char_board: 1D array of characters
        '''

        self.mask_horizontal = bb(0)
        self.mask_vertical = bb(0)
        self.pieces: dict[str, Piece] = {}

        if char_board is not None:
            if len(char_board) != HEIGHT * WIDTH:
                print('Invalid char_board')
                return

            char_board = np.array(char_board)

            for label in np.unique(char_board):
                if label == '.' or label == 'o':
                    continue

                positions = np.where(char_board == label)[0]

                pos = positions[0]
                length = len(positions)
                stride = positions[1] - positions[0]

                new_piece = Piece(pos, length, stride)

                self.pieces[label] = new_piece

                if stride == H:
                    self.mask_horizontal |= new_piece.get_mask()
                elif stride == V:
                    self.mask_vertical |= new_piece.get_mask()
        

    def get_mask(self):
        return self.mask_horizontal | self.mask_vertical
    
    def get_enum(self):
        return EnumBoard(self.mask_horizontal, self.mask_vertical)

    def add_piece(self, label, new_piece):
        if label in self.pieces:
            print(f'{label} existed')
        else:
            self.pieces[label] = new_piece
            stride = self.pieces[label].get_stride()
            
            if stride == H:
                self.mask_horizontal |= self.pieces[label].get_mask()
            elif stride == V:
                self.mask_vertical |= self.pieces[label].get_mask()

    def remove_piece(self, label):
        if label in self.pieces:
            stride = self.pieces[label].get_stride()
    
            if stride == H:
                self.mask_horizontal &= ~self.pieces[label].get_mask()
            elif stride == V:
                self.mask_vertical &= ~self.pieces[label].get_mask()

            del self.pieces[label]

    def move_piece(self, move: Move, generate_copy = False):
        '''
        Apply a move on current board

        INPUT:
            move (Move): Specific the movement
            copy (bool): True if you want to make a copy, else False
        OUTPUT:
            new_board (Board): A new board after applying move (just return if copy = True)
        '''

        if not generate_copy:
            cur_piece = self.pieces[move.label]

            if cur_piece.get_stride() == H:
                self.mask_horizontal &= ~cur_piece.get_mask()
                cur_piece.move(move.steps)
                self.mask_horizontal |= cur_piece.get_mask()
            else:
                self.mask_vertical &= ~cur_piece.get_mask()
                cur_piece.move(move.steps)
                self.mask_vertical |= cur_piece.get_mask()
        else:
            new_board = copy.deepcopy(self)
            new_board.move_piece(move, generate_copy=False)
            return new_board


    def get_legal_moves(self, previous_move: Move = None):
        '''
        Generate all legal single moves (moves just 1 step)

        INPUT:
            previous_move (move): None if don't want to ignore previous move, else ignore it's undo_step from legal moves 
        OUTPUT: 
            legal_moves (list of moves): A list of legal moves that can be applied on current board
        '''
        legal_moves = []
        mask = self.mask_horizontal | self.mask_vertical

        for label in self.pieces:
            pos, length, stride = self.pieces[label].get_attributes()            

            if stride == H:
                left, right = pos - H, pos + H * length
                if left >= 0 and left // WIDTH == pos // WIDTH and not (int(mask) >> left) & 1:
                    legal_moves.append(Move(label, -1))

                if right < HEIGHT * WIDTH and right // WIDTH == pos // WIDTH and not (int(mask) >> right) & 1:
                    legal_moves.append(Move(label, 1))

            elif stride == V:
                top, bottom = pos - V, pos + V * length
                if top >= 0 and not (int(mask) >> top) & 1:
                    legal_moves.append(Move(label, -1))
                
                if bottom < HEIGHT * WIDTH and not (int(mask) >> bottom) & 1:
                    legal_moves.append(Move(label, 1))
        
        
        if previous_move is not None and previous_move.undo_move() in legal_moves:
            legal_moves.remove(previous_move.undo_move())

        return legal_moves

    def is_goal(self):
        if MAIN_LABEL in self.pieces:
            if self.pieces[MAIN_LABEL].get_mask() == 0xC:
                return True
        return False

    def print(self):
        new_board = [' ' for _ in range(HEIGHT * WIDTH)]

        for label in self.pieces:
            pos = self.pieces[label].get_position()
            length = self.pieces[label].get_length()
            stride = self.pieces[label].get_stride()

            for _ in range(length):
                new_board[pos] = label
                pos += stride
            
        new_board = np.array(new_board).reshape((HEIGHT, WIDTH))
        print(new_board)
