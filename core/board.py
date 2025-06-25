import numpy as np
from bitboard import bb
from piece import piece
from constants import HEIGHT, WIDTH, H, V
from solution import move

class board:
    def __init__(self, char_board = None):
        '''
        Input:
            char_board: 1D array of characters
        '''

        self.bb_Horizontal = bb(0)
        self.bb_Vertical = bb(0)
        self.pieces = {}

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

                new_piece = piece(pos, length, stride)

                self.pieces[label] = new_piece

                if stride == H:
                    self.bb_Horizontal |= new_piece.get_mask()
                elif stride == V:
                    self.bb_Vertical |= new_piece.get_mask()
        

    def get_mask(self):
        return self.bb_Horizontal | self.bb_Vertical

    def get_horizontal_mask(self):
        return self.bb_Horizontal

    def get_vertical_mask(self):
        return self.bb_Vertical

    def add_piece(self, label, new_piece):
        if label in self.pieces:
            print(f'{label} existed')
        else:
            self.pieces[label] = new_piece

    def remove_piece(self, label):
        if label in self.pieces:
            del self.pieces[label]

    def move_piece(self, move):
        cur_piece = self.pieces[move.label]

        if cur_piece.get_stride() == H:
            self.bb_Horizontal &= ~cur_piece.get_mask()
            cur_piece.move(move.steps)
            self.bb_Horizontal |= cur_piece.get_mask()
        else:
            self.bb_Vertical &= ~cur_piece.get_mask()
            cur_piece.move(move.steps)
            self.bb_Vertical |= cur_piece.get_mask()

    def get_legal_moves(self, previous_move = None):
        '''
        INPUT:
            previous_move (move): None if don't want to ignore previous move, else ignore it from legal moves 
        OUTPUT: 
            legal_moves: A list of legal moves that can be applied on current board
        '''
        legal_moves = []
        
        return legal_moves

    def is_goal(self):
        pass

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


def generate_move(first_board, second_board):
    
    '''
    Generate a legal move that transforms first_board --> second_board

    INPUT:
        first_board (board): Board before applying movement
        Second_board (board): Board after applying movement
    OUTPUT:
        transfrom_move (move): The move that transforms first_board --> second_board
    '''
    pass

# char_board = list("a.bacb.c.")
# b = board(char_board)
# b.print()
# b.move_piece(move('a', 1))
# print('After move "a" by 1 step: ')
# b.print()