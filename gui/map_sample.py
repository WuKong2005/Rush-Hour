import random
from core.board import Board

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
    
MAXIMUM_MAPS = 12