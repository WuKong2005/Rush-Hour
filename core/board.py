import numpy as np
from bitboard import bb, printBitBoard
from piece import piece

height = 3
width = 3

H = 1
V = 3

class board:
    def __init__(self, char_board = None):
        '''
        Argument:
            char_board: 1D array of characters
        '''

        self.bb_Horizontal = bb(0)
        self.bb_Vertical = bb(0)
        self.pieces = {}

        if char_board is not None:
            if len(char_board) != height * width:
                print('Invalid char_board')
                return

            char_board = np.array(char_board)

            for label in np.unique(char_board):
                if label == '.':
                    continue

                positions = np.where(char_board == label)[0]

                pos = positions[0]
                length = len(positions)
                stride = positions[1] - positions[0]

                new_piece = piece(pos, length, stride)

                self.pieces[label] = new_piece

                if stride == H:
                    self.bb_Horizontal |= new_piece.get_mask()
                else:
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

    def move_piece(self, label, steps):
        cur_piece = self.pieces[label]

        if cur_piece.get_stride() == H:
            self.bb_Horizontal &= ~cur_piece.get_mask()
            cur_piece.move(steps)
            self.bb_Horizontal |= cur_piece.get_mask()
        else:
            self.bb_Vertical &= ~cur_piece.get_mask()
            cur_piece.move(steps)
            self.bb_Vertical |= cur_piece.get_mask()

    def is_goal(self):
        pass

    def print(self):
        new_board = [' ' for _ in range(height * width)]

        for label in self.pieces:
            pos = self.pieces[label].get_position()
            length = self.pieces[label].get_length()
            stride = self.pieces[label].get_stride()

            for _ in range(length):
                new_board[pos] = label
                pos += stride
            
        new_board = np.array(new_board).reshape((height, width))
        print(new_board)


char_board = list("a.bacb.c.")

b = board(char_board)

b.print()

b.move_piece('a', 1)

print('After move "a" by 1 step: ')

b.print()