from Board import Board
from search_algorithm.bfs import bfs
from search_algorithm.dfs import dfs
from search_algorithm.ucs import ucs
from search_algorithm.a_star import a_star
from Solution import Move, Solution
from search_algorithm.Node import Node
import copy
import time


class Solver:
    algo_map = {
        'bfs'   : bfs,
        'dfs'   : dfs,
        'ucs'   : ucs,
        'a_star': a_star
    }

    def __init__(self, init_board: Board = None, algorithm: str = None):
        self.init_board = init_board
        self.algorithm = algorithm

        self.solution = Solution()
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

        self.solution, self.num_expanded_state = self.algo_map[self.algorithm](Node(current_state = self.init_board), count_expanded)
        
        end_time = time.time() if measure_time else 0
        self.time = end_time - start_time

    def print_solution(self):
        board = copy.deepcopy(self.init_board)
        list_moves = self.solution.get_solution()
        for move in list_moves:
            move.print()
            board.move_piece(move)
            board.print()
            print()