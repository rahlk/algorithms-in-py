import time
import random
import unittest 
from pdb import set_trace
from sort import heapsort, mergesort,mergesort_dynamic, quicksort
from datastructures.heap import Heap


class TestSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSort, self).__init__(*args, **kwargs)

    def test_heapsort(self):
        for _ in range(500):
            raw_array = [round(random.random(), 2) for n in range(100)]
            default_sort = sorted(raw_array)
            sorted_array = heapsort(raw_array)
            self.assertEqual(sorted_array, default_sort)
        
    def test_mergesort(self):
        for _ in range(500):
            raw_array = [round(random.random(), 2) for n in range(100)]
            default_sort = sorted(raw_array)
            sorted_array = mergesort(raw_array)
            self.assertEqual(sorted_array, default_sort)

    def test_mergesort_dynamic(self):
        for _ in range(500):
            raw_array = [round(random.random(), 2) for n in range(100)]
            default_sort = sorted(raw_array)
            sorted_array = mergesort_dynamic(raw_array)
            self.assertEqual(sorted_array, default_sort)
    
    def test_quicksort(self):
        for _ in range(500):
            raw_array = [round(random.random(), 2) for n in range(100)]
            default_sort = sorted(raw_array)
            sorted_array = quicksort(raw_array)
            self.assertEqual(sorted_array, default_sort)
    
