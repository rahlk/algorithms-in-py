"""
A problem in 'The Algorithm Design Manual' 2nd Ed. by Skeina, Pg. 116-117.

Given a Heap, a number x, and a integer k, determine if the k-th smallest
item in the heap is greater than or equal to x. This must happen in O(k)
time.
"""
import os, sys
root = os.path.join(os.getcwd().split("algos-py")[0], "algos-py")
if root not in sys.path:
    sys.path.append(root)

from datastructures.heap import Heap


class Solution:
    def __init__(self): pass

    def k_th_smallest(self, heap, x, count, id):

        if count == 0 or id >= len(heap.items):
            return count
                
        if heap.items[id] < x:
            count = count - 1
            left = heap._left(id)
            right = heap._right(id)
            count = self.k_th_smallest(heap, x, count, left)
            count = self.k_th_smallest(heap, x, count, right)
        
        return count

    def main(self, heap, x, k):
        return self.k_th_smallest(heap, x, k, id = 0) > 0


if __name__ == "__main__":
    array = [25, 207, 302, 607, 334, 461, 205, 895, 966, 910]
    h = Heap(array)
    solution = Solution()
    print(solution.main(h, 900, 10))
