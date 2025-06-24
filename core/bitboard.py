import numpy as np

height = 3
width = 3

bb = np.uint64

def printBitBoard(bitboard, height = height, width = width):
    pos = np.arange(height * width, dtype=bb)
    bits = np.array((bitboard >> pos) & 1).reshape((height, width))
    board = np.where(bits == 1, 'X', '.')
    print(board)