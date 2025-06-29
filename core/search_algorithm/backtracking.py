from solution import Solution
from .Node import Node
from board import Board

solution = Solution()
visited = set()
num_expanded =[0]

def backtrack(node: Node):
    if node.is_goal():
        return True
    
    board: Board = node.current_board
    legal_moves = board.get_legal_moves()
    num_expanded[0] += 1
    visited.add(node.get_enum())

    for move in legal_moves:
        board.move_vehicle(move)

        if node.get_enum() in visited:
            board.move_vehicle(move.undo())
            continue

        if backtrack(node):
            solution.add_move(move)
            board.move_vehicle(move.undo())
            return True
        
        board.move_vehicle(move.undo())

    visited.remove(node.get_enum())

    return False

def backtracking(node: Node):
    global solution
    global visited
    global num_expanded

    solution = Solution()
    visited = set()
    num_expanded =[0]

    if backtrack(node):
        return solution, num_expanded[0]
    else:
        return None, num_expanded[0]