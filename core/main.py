from solver import Solver
from board import Board

char_board = list("BBBoooooCoooAACoooooDoooooDoooooDooo")

board = Board(char_board)
board.print()

sol = Solver(Board(char_board), 'dfs')

sol.solve(count_expanded=True)

sol.print_solution()