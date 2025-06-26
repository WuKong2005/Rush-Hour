from solver import Solver
from board import Board

char_board = list("BBBKLMHCCKLMHoAALMDDJooooIJEEooIFFGG")

board = Board(char_board)
board.print()

sol = Solver(Board(char_board), 'a_star')

sol.solve(measure_time=True, count_expanded=True)

sol.print_solution()
print(f'time: {round(sol.time, 3)} seconds')
print(f'number of expanded states: {sol.num_expanded_state}')