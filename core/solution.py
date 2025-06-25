class Move:
    def __init__(self, label, steps):
        self.label = label
        self.steps = steps

    def print(self):
        print(f'{self.label} move {self.steps} steps')

class Solution:
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