from solution import Solution
from .Node import Node
from board import Board
from constants import MAX_DEPTH

solution = Solution()
visited = set()
num_expanded =[0]
depth = [0]

def backtrack(node: Node):
    if node.is_goal():
        return True
    if depth[0] > MAX_DEPTH:
        return False
    
    board: Board = node.current_board
    legal_moves = board.get_legal_moves()
    num_expanded[0] += 1
    depth[0] += 1
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
    depth[0] -= 1

    return False

def backtracking(node: Node):
    global solution
    global visited
    global num_expanded
    global depth

    solution = Solution()
    visited = set()
    num_expanded =[0]
    depth = [0]

    if backtrack(node):
        return solution, num_expanded[0]
    else:
        return None, num_expanded[0]