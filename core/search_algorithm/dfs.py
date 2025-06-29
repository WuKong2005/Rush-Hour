from solution import Solution
from .Node import Node

def dfs_recursive(current: Node, num_expanded: list, visited: set, solution: Solution):
    successors = current.generate_successors()    
    num_expanded[0] += 1

    for child in successors:
        if child.get_enum() in visited:
            continue
        if child.is_goal():
            solution.add_move(child.get_previous_move())
            return True

        visited.add(child.get_enum())
        if dfs_recursive(child, num_expanded, visited, solution):
            solution.add_move(child.get_previous_move())
            return True
        visited.remove(child.get_enum())

    return False

def dfs(node: Node):
    '''
    Apply Depth-First Search (DFS) algorithm.

    Parameters:
        node (Node): The initial state of the search.

    Returns:
        solution (Solution): Object for backtracking the solution path.
        num_expanded (int): Number of expanded states (if count_expanded is True).
    '''
    num_expanded = [0]
    # Set of EnumBoard
    visited = set()
    visited.add(node.get_enum())
    solution = Solution()

    if node.is_goal():
        return solution, num_expanded[0]
    
    if dfs_recursive(node, num_expanded, visited, solution):
        return solution, num_expanded[0]
    else:
        return None, num_expanded[0]