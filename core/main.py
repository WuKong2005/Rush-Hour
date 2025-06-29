from solver import Solver
from board import Board

char_board = list("ooEFBBooEFoHAAEooHDoooGIDCCoGIDooooo")

board = Board(char_board)

sol = Solver(Board(char_board), 'a_star')

sol.solve()

# sol.print_solution()
print(f'number of steps: {sol.get_solution_steps()}')
print(f'time: {round(sol.time, 3)} seconds')
print(f'memory usage: {round(sol.memory, 3)} KB')
print(f'number of expanded nodes: {sol.num_expanded_state}')