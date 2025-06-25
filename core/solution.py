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