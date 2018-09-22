from pdb import set_trace


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
    visited = []
    stack = [start]

    # Explore until the stack is empty
    while stack:
        # Obtain the next node
        next = stack.pop()

        # If the next node has not been seen before
        if next not in visited:
            # Add the next in the visited list
            visited.append(next)
            # Add the adjacent nodes to the stack
            stack.extend(graph[next])

    # Return exploration order
    return visited


def dfs_recr(graph, start):
        pass


def bfs(graph, start):
    """
    Breadth First Search that uses queues
    
    Parameters
    ----------
    graph: dict
        A dictionary representing adjacency lists
    start: str
        A starting vertex

    
    Returns
    -------
    list
        Order of traversal in BFS 
    """

    visited = [start]  # Initialize visited
    queue = [start]  # Initialize traversal queue
    order = []  # Initialize order of traversal list
    
    while len(queue): # Repeat until the queue is empty
        next_ = queue.pop(0)  # Pop the leftmost element
        order.append(next_)  # Append that to the traversal order list
        visited.append(next_)  # Append that to the visited list
        neigh = graph[next_]  # Obtain the neighbors of the current vertex
        for v in neigh:
            if v not in visited:  
                # If the neighbor hasn't been visited, enqueue.
                queue.append(v)

    # Finally, return traversal order order.
    return order


def bfs_recr(graph, start):
    pass


if __name__ == "__main__":

    graph = {
        '0': ['1', '2'],
        '1': ['2'],
        '2': ['0', '3'],
        '3': ['3'],
    }

    start = '2'
    order = bfs(graph, start)

    print(" -> ".join(order))
