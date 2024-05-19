#Easy
#Array / String
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,val in enumerate(nums):
            sub = target-val
            if sub in seen:
                return[seen[sub],i]
            seen[val]=i 
        return []