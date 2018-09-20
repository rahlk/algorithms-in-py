def dfs(graph, start):
    """
    Perform a depth first search using stacks

    Parameters
    ----------
    graph: dict
        A dictionary representing adjacency lists
    start: str
        A starting vertex

    Returns
    -------
    list:
        Order in which the vertices are visited in a DFS
    """

    # Initialize visited node and stack
    visited = set()
    stack = [start]

    # Explore until the stack is empty
    while stack:
        # Obtain the next node
        next = stack.pop()

        # If the next node has not been seen before
        if next not in visited:
            # Include the next in the visited list
            visited.append(next)
            # Add the adjacent nodes to the stack
            stack.extend(graph[next] - visited)

    # Return exploration order
    return visited

def dfs_recr(graph, start):
    pass


def bfs(graph, start):
    pass


def bfs_recr(graph, start):
    pass


if __name__ == "__main__":

    graph =  {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }

    start = 'A'
    order = dfs(graph, start)

    print(order)
