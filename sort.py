import random
from pdb import set_trace
from datastructures.heap import Heap


def _merge(one, two):
    """
    Merge two arrays
    
    Parameters
    ----------
    one : list
        A sorted array
    two : list
        A sorted array
    
    Returns
    -------
    list
        Merged array
    
    Notes
    -----
    1.  The intuition here is that the two arrays are sorted. So the smallest 
        element in each of the arrays is always on the top. 
    2.  So, we can compare the two topmost elements and save the least until 
        both the arrays are exhausted.
    """
    aux = []

    while one and two:
        if one[0] < two[0]:
            next_ = one.pop(0)
        else:
            next_ = two.pop(0)
        aux.append(next_)

    aux.extend(one)
    aux.extend(two)
    return aux


def heapsort(raw_array):
    """
    Perform heapsort
    
    Parameters
    ----------
    raw_array : list
        Unsorted array
    
    Returns
    -------
    list
        Sorted array
    """
    heap = Heap(raw_array)
    sorted_array = [heap.extract_min() for _, __ in enumerate(raw_array)]
    return sorted_array


def mergesort(raw_array):
    """
    Perform merge sort.
    
    Parameters
    ----------
    raw_array : list
        An array of unsorted numbers
    
    Returns
    -------
    list
        Sorted array
    
    Notes
    -----
    1.  Divide the array in two approximately equal halves (left and right)
    2.  Recurse on the left array
    3.  Recurse on the right array
    4.  Merge the two arrays
    """

    if len(raw_array) == 1:
        return raw_array

    numel = len(raw_array)
    left = raw_array[:int(numel/2)]
    right = raw_array[int(numel/2):]

    return _merge(mergesort(left), mergesort(right))


def mergesort_dynamic(raw_array):
    """
    Perform merge sort with dynamic programming
    
    Parameters
    ----------
    raw_array : <numpy.ndarray>
        An array of unsorted numbers
    
    Returns
    -------
    <numpy.ndarray>
        Sorted array
    
    Notes
    -----
    1.  Merge pairs of elements until no pairs are left
    2.  E.g., [3,2,4,1] -> [[2,3],[1,4]] -> [[1,2,3,4]]
    """

    while len(raw_array) > 1:
        numel = len(raw_array)
        for idx in range(int(numel/2)):
            one = raw_array.pop(idx)
            two = raw_array.pop(idx)
            "It's possible that there is only one element, these must be lists"
            if not isinstance(one, list):
                one = [one]
            if not isinstance(two, list):
                two = [two]
            raw_array.insert(0, _merge(one, two))

    raw_array = raw_array[0]
    return raw_array


def quicksort(raw_array):
    """
    Quick sort
    
    Parameters
    ----------
    raw_array : list
        Unsorted array
    
    Returns
    -------
    list: 
        Sorted Array
    """
    
    numel = len(raw_array)
    
    if numel <= 1:
        return raw_array

    pivot_indx = random.randint(0, numel-1)
    pivot_item = raw_array.pop(pivot_indx)
    less = []
    more = []
    
    for item in raw_array:
        if item <= pivot_item:
            less.append(item)    
        if item > pivot_item:
            more.append(item)
    
    return quicksort(less)+[pivot_item]+quicksort(more)

    


