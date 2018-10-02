from pdb import set_trace
class Solution(object):
    
    @classmethod
    def intersect(cls, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        def bin_search(array, value):
            numel = len(array)
            mid_pt = int(numel/2)

            if len(array) == 1:
                return value if array[0] == value else None

            if array[mid_pt] == value:
                return value
        
            elif array[mid_pt] > value:
                return bin_search(array[:mid_pt], value)

            elif array[mid_pt] < value:
                return bin_search(array[mid_pt:], value)

        nums1 = sorted(nums1)  # O(mlogm)
        nums2 = sorted(nums2)  # O(nlogm)

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        intersection = []

        for num_in_1 in nums1:
            found = bin_search(nums2, num_in_1)
            if found is not None:
                intersection.append(found)

        return intersection

if __name__ == "__main__":
    main()    