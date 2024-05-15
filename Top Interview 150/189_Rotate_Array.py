#Medium
#Array / String
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        a=k%len(nums)
        if a!=0 and len(nums)>=1:
            n = len(nums)
            nums[:] = nums[n-a:]+nums[:-a]
            return nums