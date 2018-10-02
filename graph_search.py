from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self, directed=True):
        self.graph = defaultdict(set)
        self.directed = directed
    
    def add_edge(self, a, b):
        """
        Add an edge

        Add an edge between vertex a and b. 
        If undirected, add an edge between b and a too.

        Parameters
        ----------
        a : int or str
            Vertex id.
        b : int or str
            Vertex id.
        """
        self.graph[a].add(b)
        if not self.directed:
            self.graph[b].add(a)

    def bfs(self, start):
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
        dict
            Parent nodes of every vertex
        """
        visited = defaultdict(lambda: False)
        parents = defaultdict(lambda: None)
        queue = [start]
        order = []
        while queue:
            next_ = queue.pop(0)
            if not visited[next_]:
                order.append(next_)
            visited[next_] = True
            unexplored = [
                neigh for neigh in self.graph[next_] if not visited[neigh]]
            queue.extend(unexplored)
            for v in unexplored:
                if not parents[v]:
                    parents[v] = next_
        
        return order, parents
            

    def find_path(self, start, end, parents=None, path=[]):
        """
        Find the shortest path.
        
        Parameters
        ----------
        start : int or str
            Starting vertex
        end : int or str
            Ending vertex
        
        Returns
        -------
        list
            A list of vertices that takes us from start to finish.
        """
        if parents is None:
            _, parents = self.bfs(start)
        
        if start == end or end is None:
            path.insert(0, start)
        
        else:
            path.insert(0, end)
            self.find_path(start, parents[end], parents, path)
        
        return path
    
    @staticmethod
    def _complement(colour):
        if colour == 'red':
            return 'black'
        else:
            return 'red'


    def is_bipartite(self):
        """
        Determine if the graph is bipartite
        
        Returns
        -------
        bool
            True if bipartite. False otherwise.
        
        Notes
        -----
        1.  We start with a regular BFS
            a.  Initialize queue with a start node  
            b.  Color it 'red'
            c.  Repeat until empty queue
                  i. Popleft the next node
                 ii. Mark it as visited
                iii. Gather all it's neighbors
                 iv. If a neighbor is not colored, paint it the complementary 
                     color
                  v. If a neighbor is colored, and it's the same as it's 
                     predecessor, then the graph is not bipartite, return False.
                 vi. Otherwise, carry on.
            d.  Return True in the end, if we could successfully color all 
                vertices the correct color.
        """

        start = list(self.graph)[0]
        color = defaultdict(lambda: None)
        visited = defaultdict(lambda: False)
        queue = deque()
        queue.append(start)
        color[start] = 'red'

        while queue:
            next_ = queue.popleft()
            visited[next_] = True
            neigh = self.graph[next_]
            for v in neigh:
                if color[v] is None:
                    color[v] = self._complement(color[next_])
                if color[v] == color[next_]:
                    return False
                if not visited[v]:
                    queue.append(v)

        return True

        
    def dfs(self, start):
        """
        Depth First Search
        
        Parameters
        ----------
        start : int or str
            Starting node
        
        Returns
        -------
        list
            Traversal order
        """
        order = []
        stack = [start]
        visited = defaultdict(lambda: False)

        while stack:
            next_ = stack.pop()
            if not visited[next_]:
                order.append(next_)
                visited[next_] = True
                stack.extend(list(self.graph[next_]))
        
        return order


