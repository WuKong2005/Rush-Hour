from Solution import Solution
from .Node import Node

def dfs(node: Node, count_expanded: bool = False):
    '''
    Apply DFS algorithm:

    Input:
        node (Node): Initial state
        count_expanded (bool): Count number of expanded states or not
    Output:
        sol (Solution): for backtracking the solution path
        num_expanded (int) --> number of expanded states
    '''
    num_expanded = [0]

    # Set of EnumBoard
    visited = set()
    visited.add(node.get_enum())

    solution = Solution()

    def dfs_recursive(current: Node):
        if current.is_goal():
            return True
        
        successors = current.generate_successors()
        if count_expanded:
            num_expanded[0] += 1

        for child in successors:
            if child.get_enum() in visited:
                continue
            visited.add(child.get_enum())

            if dfs_recursive(child):
                solution.add_move(child.get_previous_move())
                return True

            visited.remove(child.get_enum())

        return False
    

    dfs_recursive(node)

    return solution, num_expanded