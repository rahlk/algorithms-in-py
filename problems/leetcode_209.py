from pdb import set_trace


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_ = 0
        fast = 0
        slow = 0
        max_len = 1e32

        for i in range(len(nums)):
            sum_ = sum(nums[slow:i])
            while sum_ >= s:
                fast = i
                max_len = min(fast-slow, max_len)
                sum_ -= nums[slow]
                slow += 1
        
        set_trace()
        return 0 if max_len is 1e32 else max_len

if __name__ == "__main__":
    # nums = [1, 4, 4]
    # s = 4
    nums = [2, 3, 1, 2, 4, 3]
    s = 7
    print(Solution().minSubArrayLen(s, nums))
