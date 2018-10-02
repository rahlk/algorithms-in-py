import unittest
from graph_search import Graph
from pdb import set_trace

class TestGraphSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGraphSearch, self).__init__(*args, **kwargs)
        
        # -----------------------------
        # ----- Graph 1: Directed -----
        # -----------------------------

        """
        graph1 = {
            '0': ['1', '2'],
            '1': ['2'],
            '2': ['0', '3'],
            '3': ['3'],
        }
        """
        self.graph1 = Graph(directed=True)
        self.graph1.add_edge(0, 1)
        self.graph1.add_edge(0, 2)
        self.graph1.add_edge(1, 2)
        self.graph1.add_edge(2, 0)
        self.graph1.add_edge(2, 3)
        self.graph1.add_edge(3, 3)

        # -------------------------------
        # ----- Graph 2: Undirected -----
        # -------------------------------
        
        """
        graph2 = {
            '1': ['2', '5', '6'],
            '2': ['1', '3', '5'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['1', '2', '4'],
            '6': ['1'],
        }
        """
        self.graph2 = Graph(directed=False)
        self.graph2.add_edge(1, 2)
        self.graph2.add_edge(1, 5)
        self.graph2.add_edge(1, 6)
        self.graph2.add_edge(2, 3)
        self.graph2.add_edge(2, 5)
        self.graph2.add_edge(3, 4)
        self.graph2.add_edge(4, 5)

        # -----------------------------------------
        # ----- Graph 3: Undirected Bipartite -----
        # -----------------------------------------
        
        """
        graph3 = {
            '1': ['2', '5', '6'],
            '2': ['1', '3', '4'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['1', '3', '4'],
            '6': ['1'],
        }
        """
        self.graph3 = Graph(directed=False)
        self.graph3.add_edge(1, 2)
        self.graph3.add_edge(1, 5)
        self.graph3.add_edge(1, 6)
        self.graph3.add_edge(2, 3)
        self.graph3.add_edge(2, 4)
        self.graph3.add_edge(3, 5)
        self.graph3.add_edge(4, 5)

    def test_bipartite(self):
        false_result = self.graph2.is_bipartite()
        true__result = self.graph3.is_bipartite()
        self.assertFalse(false_result)
        self.assertTrue(true__result)

    def test_dfs(self):
        start = 6
        end = 4
        obtained = self.graph2.dfs(start)
        actual1 = [6, 1, 5, 4, 3, 2]
        actual2 = [6, 1, 2, 3, 4, 5]
        self.assertTrue(obtained == actual1 or obtained == actual2)
    
    def test_bfs(self):
        start = 1
        end = 3
        order, _ = self.graph1.bfs(start)
        actual = [1, 2, 0, 3]
        self.assertEqual(actual, order)

        start = 6
        end = 4
        order, _ = self.graph2.bfs(start)
        actual = [6, 1, 2, 5, 3, 4]
        self.assertEqual(actual, order)

    def test_shortest_path(self):
        start = 1
        end = 3
        _, parents = self.graph1.bfs(start)
        shortest_path = self.graph1.find_path(start, end, parents, path=[])
        actual = [1, 2, 3]
        self.assertEqual(actual, shortest_path)

        start = 6
        end = 4
        shortest_path = self.graph2.find_path(start, end, parents=None, path=[])
        actual = [6, 1, 5, 4]
        self.assertEqual(actual, shortest_path)
