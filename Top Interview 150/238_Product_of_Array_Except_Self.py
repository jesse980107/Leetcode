#Medium
#Array / String
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rst = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            rst[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            rst[i] *= post
            post*=nums[i]
        return rst