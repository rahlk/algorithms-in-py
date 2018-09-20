import numpy as np
from pdb import set_trace


def _merge(one, two):
    """
    Merge two arrays

    Parameters
    ----------
    one : <numpy.ndarray>
        A sorted array
    two : <numpy.ndarray>
        A sorted array

    Returns
    -------
    <numpy.ndarray>
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


def mergesort(raw_array):
    """
    Perform merge sort.

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

    "It's possible that there is only one element, these must be lists"
    if not isinstance(left, list):
        left = list(left)
    if not isinstance(right, list):
        right = list(right)

    return merge(sort(left), sort(right))

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
    1.  Divide the array in two approximately equal halves (left and right)
    2.  Recurse on the left array
    3.  Recurse on the right array
    4.  Merge the two arrays
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
            raw_array.insert(idx, _merge(one, two))

    return raw_array[0]
