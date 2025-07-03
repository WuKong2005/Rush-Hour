from core.board import Board
from core.search_algorithm.bfs import bfs
from core.search_algorithm.dfs import dfs
from core.search_algorithm.backtracking import backtracking
from core.search_algorithm.ucs import ucs
from core.search_algorithm.a_star import a_star, weight_a_star
from core.solution import Solution
from core.search_algorithm.Node import Node
import copy
import time
import tracemalloc

class Solver:
    algo_map = {
        'BFS'           : bfs,
        'DFS'           : dfs,
        'Backtracking'  : backtracking,
        'UCS'           : ucs,
        'A*'            : a_star,
        'Weight A*'     : weight_a_star
    }

    def __init__(self, init_board: Board = None, algorithm: str = None):
        self.init_board = init_board
        self.algorithm = algorithm

        self.solution = Solution()
        self.num_expanded = 0
        self.memory = 0
        self.time = 0
        
    def get_init_board(self):
        return self.init_board
    
    def get_current_algorithm(self):
        return self.algorithm
    
    def get_measurements(self):
        return self.time, self.memory, self.num_expanded
    
    def get_solution_length(self):
        return self.solution.num_moves()
    
    def set_init_board(self, new_init_board: Board):
        self.init_board = new_init_board

    def set_algorithm(self, new_algorithm: str):
        self.algorithm = new_algorithm

    def solve(self, measure_memory: bool = False):
        '''
        Solve the problem by applying "self.current_algorithm" to find the path to goal state from "self.init_board" state

        Parameters:
            measure_time: If true, measure and save the time taken to solve.
            count_expanded: If true, count the number of expanded states.
        '''

        if self.algorithm not in self.algo_map:
            print('Invalid algorithm!')
            return None, None

        if measure_memory:
            tracemalloc.start()
        start_time = time.time()

        self.solution, self.num_expanded = self.algo_map[self.algorithm](Node(current_board=self.init_board))
        
        end_time = time.time()
        peak = 0
        if measure_memory:
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

        self.time = round(end_time - start_time, 3)
        self.memory = round(peak / 1024, 3)

    def is_solvable(self):
        return self.solution is not None

    def print_measurement(self, indent: str):
        if self.solution is not None:
            print(f'{indent}Number of steps             : {self.solution.num_moves()}')
        print(f'{indent}Running time                : {self.time}')
        print(f'{indent}Peak memory usage           : {self.memory} KB')
        print(f'{indent}Number of expanded nodes    : {self.num_expanded}')

    def print_solution(self):
        board = copy.deepcopy(self.init_board)
        g_cost = 0

        print(f'''
{self.algorithm} algorithm
-----------------
        ''')

        board.print()
        print(f'g_cost = {g_cost}')
        print(f'h_cost = {board.heuristic()}')
        print()

        if self.solution is not None:
            list_moves = self.solution.get_solution()
            for move in list_moves:
                move.print()
                g_cost += board.get_cost_move(move)
                board.move_vehicle(move)
                board.print()
                print(f'g_cost = {g_cost}')
                print(f'h_cost = {board.heuristic()}')
                print()

        else:
            print('No solution found!')
            
    def get_list_cost(self):
        board = copy.deepcopy(self.init_board)
        g_cost = 0
        
        list_cost = [(0, board.heuristic())]

        if self.solution is not None:
            list_moves = self.solution.get_solution()
            for move in list_moves:
                g_cost += board.get_cost_move(move)
                board.move_vehicle(move)
                list_cost.append((g_cost, board.heuristic()))
            return list_cost
        else:
            return None