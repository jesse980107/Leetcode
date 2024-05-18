#Medium
#Sliding Window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return len(nums)
        
        s = 0
        left = 0
        ans = len(nums)

        for right, val in enumerate(nums):
            s += val 
            while s >= target:
                s -= nums[left]
                ans = min(ans, right - left + 1)
                left += 1
        return ans