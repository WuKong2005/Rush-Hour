from solution import Solution
from .Node import Node
import heapq

def ucs(node: Node):
    '''
    Apply Uniform-Cost Search (UCS) algorithm.

    Parameters:
        node (Node): The initial state of the search.

    Returns:
        solution (Solution): Object for backtracking the solution path.
        num_expanded (int): Number of expanded states (if count_expanded is True).
    '''
    reached = {}
    frontier = []
    solution = Solution()
    num_expanded = 0

    reached[node.get_enum()] = 0
    heapq.heappush(frontier, (0, node))

    while frontier:
        (cost, current) = heapq.heappop(frontier)
        num_expanded += 1
        
        if current.is_goal():
            cur_node = current
            while cur_node.get_parent() is not None:
                solution.add_move(cur_node.get_previous_move())
                cur_node = cur_node.get_parent()
            
            return solution, num_expanded
        
        successors = current.generate_successors()
        for child in successors:
            path_cost = cost + current.get_cost_move(child.get_previous_move())
            if child.get_enum() not in reached or path_cost < reached[child.get_enum()]:
                reached[child.get_enum()] = path_cost
                heapq.heappush(frontier, (path_cost, child))

    return None, num_expanded