from solution import Solution
from .Node import Node

def dfs(node: Node, count_expanded: bool = False):
    '''
    Apply Depth-First Search (DFS) algorithm.

    Parameters:
        node (Node): The initial state of the search.
        count_expanded (bool): If True, count the number of expanded states.

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

    def dfs_recursive(current: Node):
        successors = current.generate_successors()
        if count_expanded:
            num_expanded[0] += 1

        for child in successors:
            if child.get_enum() in visited:
                continue
            if child.is_goal():
                solution.add_move(child.get_previous_move())
                return True

            visited.add(child.get_enum())
            if dfs_recursive(child):
                solution.add_move(child.get_previous_move())
                return True
            visited.remove(child.get_enum())

        return False
    
    if dfs_recursive(node):
        return solution, num_expanded[0]
    else:
        return None, num_expanded[0]