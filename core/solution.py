class Move:
    def __init__(self, label, steps):
        self.label = label
        self.steps = steps

    def __eq__(self, other):
        return isinstance(other, Move) and self.label == other.label and self.steps == other.steps

    def undo_move(self):
        undo = Move(self.label, -self.steps)
        return undo

    def print(self):
        print(f'{self.label} move {self.steps} steps')

# List of Moves
class Solution:
    def __init__(self):
        self.moves = []

    def add_move(self, new_move: Move):
        self.moves.insert(0, new_move)
    
    def pop_move(self):
        if self.moves:
            self.moves.pop()
    
    def num_move(self):
        return len(self.moves)
    
    def is_empty(self):
        return len(self.moves) == 0
    
    def get_solution(self):
        return self.moves
