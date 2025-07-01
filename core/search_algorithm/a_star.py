from solution import Solution
from .Node import A_star_node, Node
import heapq

def a_star(node: Node):
    '''
    Apply A* algorithm.

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

    node = A_star_node(0, 'heuristic', node)
    reached[node.get_enum()] = node.heuristic()
    heapq.heappush(frontier, node)

    while frontier:
        new_node: A_star_node = heapq.heappop(frontier)
        num_expanded += 1

        if new_node.is_goal():
            cur_node = new_node
            while cur_node.get_parent() is not None:
                solution.add_move(cur_node.get_previous_move())
                cur_node = cur_node.get_parent()
            
            return solution, num_expanded

        successors = new_node.generate_successors()
        for child in successors:
            enum = child.get_enum()
            if enum not in reached or child.get_f_cost() < reached[enum]:
                reached[enum] = child.get_f_cost()
                heapq.heappush(frontier, child)

    return None, num_expanded


def weight_a_star(node: Node):
    '''
    Apply A* algorithm.

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

    node = A_star_node(0, 'weight heuristic', node)
    reached[node.get_enum()] = node.heuristic()
    heapq.heappush(frontier, node)

    while frontier:
        new_node: A_star_node = heapq.heappop(frontier)
        num_expanded += 1

        if new_node.is_goal():
            cur_node = new_node
            while cur_node.get_parent() is not None:
                solution.add_move(cur_node.get_previous_move())
                cur_node = cur_node.get_parent()
            
            return solution, num_expanded

        successors = new_node.generate_successors()
        for child in successors:
            enum = child.get_enum()
            if enum not in reached or child.get_f_cost() < reached[enum]:
                reached[enum] = child.get_f_cost()
                heapq.heappush(frontier, child)

    return None, num_expanded