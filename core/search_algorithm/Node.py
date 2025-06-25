from Board import Board
from Solution import Move

class Node:
    def __init__(self, previous_move: Move = None, current_state: Board = None):
        self.previous_move = previous_move
        self.current_state = current_state

    def get_previous_move(self):
        return self.previous_move
    
    def get_current_state(self):
        return self.current_state
    
    def generate_successors(self):
        successors = []
        legal_moves = self.current_state.get_legal_moves(self.previous_move)

        for move in legal_moves:
            successors.append(Node(move, self.current_state.move_piece(move, True)))
        
        return successors
    
    def generate_parent(self):
        if self.previous_move is not None:
            label, steps = self.previous_move
            parent = self.current_state.move_piece(Move(label, -steps), generate_copy=True)
            return parent
        
        return None
    
    def is_goal(self):
        return self.current_state.is_goal()
    
    def print(self):
        self.current_state.print()