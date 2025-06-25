from Solver import Solver
from Board import Board
from Solution import Move

char_board = list("aa.bc.dbc.db....")

board = Board(char_board)

sol = Solver(Board(char_board), 'dfs')

sol.solve()