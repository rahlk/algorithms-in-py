from pdb import set_trace

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # ---- Brute Force ------
        # numel = len(nums)
        # sum_ = 0
        # max_len = 0
        # for i,val_i in enumerate(nums):
        #     sum_ = val_i
        #     for j in range(i+1, numel):
        #         sum_ += nums[j]
        #         if sum_ == k:
        #             max_len = max(max_len, j+1-i)

        # ------- Time: O(n) Space: O(n) -----
        sums_dict = dict()
        numel = len(nums)
        sum_ = 0
        max_len = 0
        for i, val in enumerate(nums):
            sum_ += val

            if sum_ == k:
                max_len = max(max_len, i+1)
            
            if sum_ not in sums_dict:
                sums_dict.update({sum_ : i})
            
            remaining = sum_ - k

            if remaining in sums_dict:
                max_len = max(max_len, i - sums_dict[remaining])


        return max_len

if __name__ == "__main__":
    nums = [1,-1,5,-2,3]
    k = 3
    s = Solution()
    print(s.maxSubArrayLen(nums, k))