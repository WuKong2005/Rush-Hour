from board import board
from search_algorithm import bfs, dfs, ucs, a_star
import time

class move:
    def __init__(self, label, steps):
        self.label = label
        self.steps = steps


class solution:
    def __init__(self):
        self.moves = []

    def add_move(self, new_move):
        self.moves.append(new_move)
    
    def pop_move(self):
        if self.moves:
            self.moves.pop()
    
    def num_move(self):
        return len(self.moves)
    
    def is_empty(self):
        return len(self.moves) == 0


class solver:
    algo_map = {
        'bfs'   : bfs,
        'dfs'   : dfs,
        'ucs'   : ucs,
        'a_star': a_star
    }

    def __init__(self, init_board = None, algorithm = None):
        self.init_board = init_board
        self.algorithm = algorithm

        self.solution = solution()
        self.num_expanded_state = 0
        self.time = 0
        
    def get_init_board(self):
        return self.init_board
    
    def get_current_algorithm(self):
        return self.algorithm
    
    def get_measurement(self):
        return self.time, self.num_expanded_state
    
    def set_init_board(self, new_init_board):
        self.init_board = new_init_board

    def set_algorithm(self, new_algorithm):
        self.algorithm = new_algorithm


    def solve(self, measure_time = False, count_expanded = False):
        if self.algorithm not in self.algo_map:
            print('Invalid algorithm!')
            return None, None

        start_time = time.time() if measure_time else 0

        self.solution, self.num_expanded_state = self.algo_map[self.algorithm](self.init_board, count_expanded)
        
        end_time = time.time() if measure_time else 0
        self.time = end_time - start_time