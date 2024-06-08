#Medium
#Array / String

# if no 0 contain in nums:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
        ans = [int(total/i) for i in nums]
        return ans
    
# for arbitrary nums:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return [0 for i in nums]
        elif nums.count(0) == 1:
            ans = []
            total = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    total *= nums[i]
            for i in range(len(nums)):
                if nums[i] != 0:
                    ans.append(0)
                else:
                    ans.append(total)
            return ans
        else:
            total = 1
            for i in range(len(nums)):
                total *= nums[i]
            ans = [int(total/i) for i in nums]
            return ans
        

