import numpy as np
from constants import HEIGHT, WIDTH

bb = np.uint64

def printBitBoard(bitboard, height = HEIGHT, width = WIDTH):
    pos = np.arange(height * width, dtype=bb)
    bits = np.array((bitboard >> pos) & 1).reshape((height, width))
    board = np.where(bits == 1, 'X', '.')
    print(board)