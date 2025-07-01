from board import Board
from solution import Move

class Node:
    def __init__(self, previous_move: Move = None, current_board: Board = None, parent: "Node" = None):
        self.previous_move = previous_move
        self.current_board = current_board
        self.parent = parent

    def __eq__(self, other: "Node"):
        return True

    def get_previous_move(self):
        return self.previous_move
    
    def get_current_board(self) -> Board:
        return self.current_board
    
    def get_parent(self):
        return self.parent
    
    def get_enum(self):
        return self.current_board.board_to_enum()
    
    def get_cost_move(self, move: Move):
        return self.current_board.get_cost_move(move)
    
    def generate_successors(self) -> list["Node"]:
        successors = []
        legal_moves = self.current_board.get_legal_moves()

        for move in legal_moves:
            new_board = self.current_board.move_vehicle(move, True)
            successors.append(Node(move, new_board, self))
        
        return successors
    
    def is_goal(self):
        return self.current_board.is_goal()
    

class A_star_node (Node):
    def __init__(self, g_cost: int, heuristic: str, node: Node):
        super().__init__(node.previous_move, node.current_board, node.parent)
        self.g_cost = g_cost
        self.heuristic_name = heuristic

        if heuristic == 'heuristic':
            self.f_cost = self.g_cost + self.heuristic()
        elif heuristic == 'weight heuristic':
            self.f_cost = self.g_cost + self.weight_heuristic()

    def __lt__(self, other: "A_star_node"):
        return self.f_cost < other.f_cost
    
    def __eq__(self, other: "A_star_node"):
        return self.f_cost == other.f_cost
    
    def get_f_cost(self):
        return self.f_cost

    def generate_successors(self) -> list["A_star_node"]:
        successors = []
        legal_moves = self.current_board.get_legal_moves()

        for move in legal_moves:
            new_board = self.current_board.move_vehicle(move, True)
            cost = self.get_cost_move(move)
            successors.append(A_star_node(self.g_cost + cost, self.heuristic_name, Node(move, new_board, self)))
        
        return successors
    
    def heuristic(self):
        return self.current_board.heuristic()
    
    def weight_heuristic(self):
        return self.current_board.heuristic() << 3