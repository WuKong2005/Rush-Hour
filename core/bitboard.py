import numpy as np
from constants import height, width

bb = np.uint64

def printBitBoard(bitboard, height = HEIGHT, width = WIDTH):
    pos = np.arange(HEIGHT * WIDTH, dtype=bb)
    bits = np.array((bitboard >> pos) & 1).reshape((HEIGHT, WIDTH))
    board = np.where(bits == 1, 'X', '.')
    print(board)