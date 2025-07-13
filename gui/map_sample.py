import random
from core.board import Board

DESIGNED_MAP = [
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

def get_random_maps(filename: str, k: int):
    """Reservoir sampling"""
    selected_lines = [str()] * k
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            j = random.randint(0, i)
            if j < k:
                selected_lines[j] = line.strip()
    
    selected_maps = []
    for line in selected_lines:
        _, map, cluster_size = line.split()
        selected_maps.append(map)
    return selected_maps
                
def init_board(selected_maps: list[str], index: int):
    if index < len(selected_maps):
        return Board(list(selected_maps[index]))
    
MAXIMUM_MAPS = 13