from solution import Solution
from .Node import Node
from board import Board
from solution import Move
from collections import deque

def backtracking(node: Node):
    num_expanded = 0
    solution = Solution()
    legal_moves = {}
    stack = deque()
    visited = set()

    state: Board = node.get_current_board()
    stack.append((0, None)) #current index and undo_move

    while stack:
        index, undo = stack.pop()

        if state.is_goal():
            solution.add_move(undo.undo())
            state.move_vehicle(undo)
            while stack:
                _, undo = stack.pop()
                if undo is not None:
                    solution.add_move(undo.undo())
                    state.move_vehicle(undo)
            
            return solution, num_expanded
        
        if index == 0:
            num_expanded += 1
        enum = state.board_to_enum()
        legal_moves[enum] = state.get_legal_moves()
        visited.add(enum)

        if index >= len(legal_moves[enum]):
            visited.remove(enum)
            del legal_moves[enum]
            if undo is not None:
                state.move_vehicle(undo)
            continue

        move: Move = legal_moves[enum][index]
        stack.append((index + 1, undo))

        state.move_vehicle(move)

        if state.board_to_enum() in visited:
            state.move_vehicle(move.undo())
            continue

        stack.append((0, move.undo()))

    return None, num_expanded


# solution = Solution()
# visited = set()
# num_expanded =[0]

# def backtrack(node: Node):
#     if node.is_goal():
#         return True
    
#     board: Board = node.current_board
#     legal_moves = board.get_legal_moves()
#     num_expanded[0] += 1
#     visited.add(node.get_enum())

#     for move in legal_moves:
#         board.move_vehicle(move)

#         if node.get_enum() in visited:
#             board.move_vehicle(move.undo())
#             continue

#         if backtrack(node):
#             solution.add_move(move)
#             board.move_vehicle(move.undo())
#             return True
        
#         board.move_vehicle(move.undo())

#     visited.remove(node.get_enum())

#     return False

# def backtracking(node: Node):
#     global solution
#     global visited
#     global num_expanded

#     solution = Solution()
#     visited = set()
#     num_expanded =[0]

#     if backtrack(node):
#         return solution, num_expanded[0]
#     else:
#         return None, num_expanded[0]