from solver import Solver
from board import Board

list_algo = [
    # 'DFS',
    # 'Backtracking',
    # 'BFS',
    # 'UCS',
    # 'A*',
    'Weight A*'
]
list_board = [
    # "BBoJoooHoJCCGHAAKLGDDoKLooIEEoFFIooo",
    # "BBHooKFoHoJKFAAoJLoGCCoLoGoIDDEEoIoo",
    # "oBBCCooooJDDAAoJKoHoEEKLHoIFFLGGIooo",
    # "BBBKLMHCCKLMHoAALMDDJooooIJoEEoIFFGG",
    # "GBBoLoGHIoLMGHIAAMCCCKoMooJKDDEEJFFo",
    # "ooIBBBooIKooAAJKoLCCJDDLGHEEoLGHFFoo",
    # "IBBCCMIoJDDMAAJKoooooKEEFFFoLoGGHHLo",
    # "ooBBBFooCooFAACooFooCooDooEEEDoooooo",
    # "oBBBooooEFooAAEFGGoCCDDooooooooooooo"
    "ooHBBoFoHICCFAAIoooGoIJKoGDDJKooEEoo"
]

for str in list_board:
    board = Board(list(str))

    print(f'\n\nBoard: {str}')
    print('-' * 20)

    for algo in list_algo:
        solver = Solver(board, algo)

        print(f'\tAlgorithm: {algo}')
        print('\t' + '-' * 20)

        print(f'\tMeasure memory:')
        solver.solve(measure_memory=True)
        solver.print_measurement(indent='\t\t')

        print('')
        print(f'\tMeasure time:')
        for _ in range(3):
            solver.solve()
            solver.print_measurement(indent='\t\t')
            print('')