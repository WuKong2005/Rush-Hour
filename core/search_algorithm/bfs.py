from solution import Solution
from .Node import Node
from collections import deque

def bfs(node: Node, count_expanded: bool = False):
    '''
    Apply Breadth-First Search (BFS) algorithm.

    Parameters:
        node (Node): The initial state of the search.
        count_expanded (bool): If True, count the number of expanded states.

    Returns:
        solution (Solution): Object for backtracking the solution path.
        num_expanded (int): Number of expanded states (if count_expanded is True).
    '''
    num_expanded = [0]

    reached = set()
    reached.add(node.get_enum())

    frontier = deque()
    frontier.append(node)

    solution = Solution()

    if node.is_goal():
        return solution, num_expanded[0]
    
    while frontier:
        current = frontier.popleft()

        if count_expanded:
            num_expanded[0] += 1

        successors = current.generate_successors()
        for child in successors:
            if child.get_enum() in reached:
                continue

            if child.is_goal():
                while child.get_parent() is not None:
                    solution.add_move(child.get_previous_move())
                    child = child.get_parent()

                return solution, num_expanded[0]
            
            reached.add(child.get_enum())
            frontier.append(child)

    return solution, num_expanded[0]