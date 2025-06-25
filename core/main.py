from Solver import Solver
from Board import Board

char_board = list("aa.bc.dbc.db....")

board = Board(char_board)
board.print()

sol = Solver(Board(char_board), 'dfs')

sol.solve(count_expanded=True)

sol.print_solution()