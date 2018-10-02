from pdb import set_trace


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        numel = len(height)
        vol = 0
        
        left_max = -1
        right_max = -1
        
        left = numel*[0]
        right = numel*[0]

        # ----- Left -----
        for idx in range(numel):
            if height[idx] > left_max:
                left_max = height[idx]
            left[idx] = left_max
        
        # ----- Right -----
        for idx in range(numel)[::-1]:
            if height[idx] > right_max:
                right_max = height[idx]
            right[idx] = right_max

        # ----- Volume -----
        for idx in range(numel):
            vol += min(left[idx], right[idx]) - height[idx]

        return vol

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(height))
