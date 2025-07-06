class Move:
    def __init__(self, label, steps):
        self.label = label
        self.steps = steps

    def __eq__(self, other):
        return isinstance(other, Move) and self.label == other.label and self.steps == other.steps
    
    def undo(self):
        return Move(self.label, -self.steps)

    def print(self):
        print(f'{self.label} move {self.steps} steps')

class Solution:
    def __init__(self):
        self.moves: list[Move] = []

    def add_move(self, new_move: Move):
        self.moves.insert(0, new_move)
    
    def pop_move(self):
        if self.moves:
            self.moves.pop(0)
    
    def num_moves(self):
        return len(self.moves)
    
    def is_empty(self):
        return len(self.moves) == 0
    
    def get_solution(self):
        return self.moves
