from core.solver import Solver
from core.board import Board

list_algo = [
    'DFS',
    'BFS',
    'UCS',
    'A*',
    'Weighted A*'
    # "Backtracking"
]
list_board = [
    "BBoJoooHoJCCGHAAKLGDDoKLooIEEoFFIooo", # Large number of states
    "BBHooKFoHoJKFAAoJLoGCCoLoGoIDDEEoIoo",
    "oBBCCooooJDDAAoJKoHoEEKLHoIFFLGGIooo",
    "BBBKLMHCCKLMHoAALMDDJooooIJoEEoIFFGG", # Large number of optimal moves
    "GBBoLoGHIoLMGHIAAMCCCKoMooJKDDEEJFFo",
    "ooIBBBooIKooAAJKoLCCJDDLGHEEoLGHFFoo",
    "ooBBBFooCooFAACooFooCooDooEEEDoooooo", # No solution
    "oBBBooooEFooAAEFGGoCCDDooooooooooooo",
    "ooHBBoFoHICCFAAIoooGoIJKoGDDJKooEEoo", # Large number of expanded nodes + backtracking is very fast
    "GoBBBLGCCJoLAAIJoooHIoDDoHEEKoFFooKo", # A* is as twice as slower than Weighted A*, WA* = 81 > A* = 80 
    "BBBooLCCIoKLAAIoKMGHDDoMGHoJEEGFFJoo", # UCS ~~ BFS
    "BBooKoCCooKoGHAAKoGHIJDDEEIJoLoFFFoL", 
    "BBoooLGIJooLGIJAAMCCJKoMHooKDDHEEFFo"  # UCS faster than BFS, and UCS expands less nodes than BFS 
]

print("MEASURE MEMORY: ")
print('-' * 20)
for str in list_board:
    board = Board(list(str))
    print(f'\n\nBoard: {str}')
    print('-' * 20)

    for algo in list_algo:
        solver = Solver(board, algo)

        solver.solve(measure_memory=True)
        print(f'\tAlgorithm: {algo} --> Memory: {solver.memory}KB')
    

print("MEASURE TIME: ")
print('-' * 20)
for str in list_board:
    board = Board(list(str))
    print(f'\n\nBoard: {str}')
    print('-' * 20)

    for algo in list_algo:
        solver = Solver(board, algo)

        print(f'\tAlgorithm: {algo}')
        print('\t' + '-' * 20)

        time = 0
        length = 0
        cost = 0
        expanded = 0

        solver.solve()
        time, _, expanded = solver.get_measurements()
        length = solver.get_solution_length()
        cost = solver.get_solution_cost()

        for _ in range(4):
            solver.solve()
            time += solver.time
        
        time = round(time / 5, 3)

        print(f'\t\tSolution Depth: {length}')
        print(f'\t\tSolution cost : {cost}')
        print(f'\t\tRuntime       : {time}')
        print(f'\t\tExpanded Nodes: {expanded}')
