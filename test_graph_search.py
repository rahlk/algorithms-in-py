import unittest
from graph_search import dfs, dfs_recr, bfs, bfs_recr
from pdb import set_trace

class TestGraphSearch(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGraphSearch, self).__init__(*args, **kwargs)
        self.graph =  {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E'])
        }
        self.start_node = 'A'

    def test_dfs(self):
        assert False

    def test_dfs_recr(self):
        assert False

    def test_bfs(self):
        assert False

    def test_bfs_recr(self):
        assert False
