from Board import Board
from Solution import Move

class Node:
    def __init__(self, previous_move: Move = None, current_state: Board = None, parent: "Node" = None):
        self.previous_move = previous_move
        self.current_state = current_state
        self.parent = parent

    def get_previous_move(self):
        return self.previous_move
    
    def get_current_state(self):
        return self.current_state
    
    def get_parent(self):
        return self.parent
    
    def generate_successors(self):
        successors = []
        legal_moves = self.current_state.get_legal_moves()

        for move in legal_moves:
            new_board = self.current_state.move_piece(move, True)
            successors.append(Node(move, new_board, self))
        
        return successors
    
    def get_enum(self):
        return self.current_state.get_enum()
    
    def is_goal(self):
        return self.current_state.is_goal()
    
    def print(self):
        self.current_state.print()