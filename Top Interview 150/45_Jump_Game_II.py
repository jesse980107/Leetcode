#Medium
#Array / String
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        l=r=0
        while r< len(nums)-1:
            curr = 0
            for i in range(l,r+1):
                curr = max(curr, i+nums[i])
            l=r+1
            r = curr
            jump+=1

        return jump