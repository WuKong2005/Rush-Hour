import numpy as np
from core.constants import HEIGHT, WIDTH

bb = np.uint64

def printBitBoard(bitboard, height = HEIGHT, width = WIDTH):
    pos = np.arange(HEIGHT * WIDTH, dtype=bb)
    bits = np.array((bitboard >> pos) & 1).reshape((HEIGHT, WIDTH))
    board = np.where(bits == 1, 'X', '.')
    print(board)