from board import Board
from search_algorithm.bfs import bfs
from search_algorithm.dfs import dfs
from search_algorithm.ucs import ucs
from search_algorithm.a_star import a_star
from solution import Solution
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
    
    def set_init_board(self, new_init_board: Board):
        self.init_board = new_init_board

    def set_algorithm(self, new_algorithm: str):
        self.algorithm = new_algorithm

    def solve(self, measure_time: bool = False, count_expanded: bool = False):
        '''
        Solve the problem by applying "self.current_algorithm" to find the path to goal state from "self.init_board" state

        Parameters:
            measure_time: If true, measure and save the time taken to solve.
            count_expanded: If true, count the number of expanded states.
        '''

        if self.algorithm not in self.algo_map:
            print('Invalid algorithm!')
            return None, None

        start_time = time.time() if measure_time else 0

        self.solution, self.num_expanded_state = self.algo_map[self.algorithm](Node(current_state = self.init_board), count_expanded)
        
        end_time = time.time() if measure_time else 0
        self.time = end_time - start_time

    def is_solvable(self):
        return self.solution is not None

    def print_solution(self):
        board = copy.deepcopy(self.init_board)
        if self.solution is not None:
            list_moves = self.solution.get_solution()
            for move in list_moves:
                move.print()
                board.move_piece(move)
                board.print()
                print()