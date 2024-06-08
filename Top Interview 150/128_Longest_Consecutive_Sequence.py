#Medium
#Array / String
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in nums:
                x = n + 1
                while x in nums:
                    x += 1
                res = max(res, x - n)
        return res