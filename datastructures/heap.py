from numpy import log2
from copy import deepcopy

class Heap:
    """
    A Heap Datastructure    
    """

    def __init__(self, array, alt_makeheap=True):
        self.items = []
        if alt_makeheap:
            "Alternative makeheap that uses bubble down."
            self.fast_makeheap(array)
        else:
            self.makeheap(array)

    def _left(self, idx):
        """
        Left child.
        
        Parameters
        ----------
        idx : int
            Index of the parent
        
        Returns
        -------
        int
            Index of the left child. -1 if parent is leaf.
        """

        left = idx * 2 + 1
        if left >= len(self.items):
            return -1
        else:
            return left

    def _right(self, idx):
        """
        Right child.
        
        Parameters
        ----------
        idx : int
            Index of the parent
        
        Returns
        -------
        int
            Index of the right child. -1 if parent is left.
        """

        right = (idx + 1) * 2
        if right >= len(self.items):
            return -1
        else:
            return right

    def _parent(self, idx):
        """
        Parent of a child node.
        
        Parameters
        ----------
        idx : int
            Index of the child
        
        Returns
        -------
        int
            Index of the parent. -1 if the child is root.
        """

        if idx == 0:
            return -1
        else:
            return int((idx - 1) / 2)

    def _bubble_up(self, idx):
        """
        A bubble-up operation

        Parameters
        ----------
        idx: int
            Index of the current node.
        
        Returns
        -------
        self: self
            The current heap is returned.

        Notes
        -----
        1.  Check if the parent is -1. If so, we are already at the root, do 
            nothing.
        2.  Otherwise, if the parent is smaller (assuming min-heap), swap the
            parent with the child.
        3.  Recurse on the parent.
        """

        parent = self._parent(idx)
        if parent == -1:
            return self

        if self.items[parent] > self.items[idx]:
            self.items[idx], self.items[parent] = \
                self.items[parent], self.items[idx]
            self._bubble_up(parent)

    def insert(self, item):
        """
        Insert a new item into the heap. 

        Parameters
        ----------
        item: int or float
            Item to be inserted into the heap

        Returns
        -------
        self: self
            The current heap is returned

        Notes
        -----
        1.  Append the new item
        2.  Set current index (called 'now') to the index of the last
            item in the heap.
        3.  Bubble up the last item
        """

        self.items.append(item)
        now = len(self.items) - 1
        return self._bubble_up(now)

    def makeheap(self, array):
        """
        Make heap from a raw array
        
        Parameters
        ----------
        array : List
            A list of raw array
        """

        for item in array:
            self.insert(item)

    def _bubble_down(self, idx):
        """
        Percolate the item down until the heap structure is respected

        Parameters
        ----------
        idx: int
            Index of the parent node
        
        Returns
        -------
        self
            Returns the updated heap
        
        Notes
        -----
        1.  Compare the parent with the left & right children.
        2.  Swap parent with the smallest child
        3.  Recurse on the smallest child
        """

        left = self._left(idx)
        right = self._right(idx)

        if left == -1 and right == -1:
            return

        next_ = left if self.items[left] < self.items[right] or right == -1 else right

        if self.items[idx] > self.items[next_]:
            self.items[idx], self.items[next_] = \
                self.items[next_], self.items[idx]
            self._bubble_down(next_)

    def extract_min(self):
        """
        Find and return the smallest item in the heap

        Parameters
        ----------
        None

        Returns
        -------
        min_: int or float
            The smallest item
        
        Notes
        -----
        1.  The smallest item is at index 0. Pop that.
        2.  Move the last item at index N-1 to position 0 (the top of the heap).
        3.  Percolate the topmost item down the heap until the structure is 
            satisifed.
        4.  Return the popped item.
        """

        if len(self.items) == 1:
            min_ = self.items.pop(0)

        if len(self.items) > 1:
            min_ = self.items[0]
            last = self.items.pop(-1)
            self.items[0] = last
            self._bubble_down(idx=0)

        return min_

    def fast_makeheap(self, array):
        """
        A linear time heap construction.
        
        See Skeina, 2nd Ed., Section 4.3.4, Page 115-116.
        
        Parameters
        ----------
        array : list
            An unsorted array
        """

        self.items = deepcopy(array)
        numel = len(self.items)
        for idx in range(2 ** int(log2(numel)))[::-1]:
            self._bubble_down(idx)


