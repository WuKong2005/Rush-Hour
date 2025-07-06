from core.solver import Solver
from core.board import Board

list_algo = [
    'DFS',
    # 'Backtracking'
    'UCS',
    'A*',
    'Weighted A*'
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

for str in list_board:
    board = Board(list(str))
    board.print()
    print(f'\n\nBoard: {str}')
    print('-' * 20)

    for algo in list_algo:
        solver = Solver(board, algo)

        print(f'\tAlgorithm: {algo}')
        print('\t' + '-' * 20)

        print(f'\tMeasure memory: ')
        solver.solve(measure_memory=True)
        solver.print_measurement(indent='\t\t')

        print('')
        # print(f'\tMeasure time:')
        # for _ in range(1):
        #     solver.solve()
        #     # solver.print_solution()
        #     solver.print_measurement(indent='\t\t')
        
        # print('')