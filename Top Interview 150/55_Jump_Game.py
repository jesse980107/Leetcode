#Medium
#Array / String
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        input = nums
        can_index = 0
        last_index= 0
        for i in range(len(input)):
            can_index = input[i]+i
            last_index = max(last_index,can_index)
            print(can_index,last_index,i,input[i])
            if can_index >=len(input)-1:
                return True
            elif input[i] == 0 and last_index<=i:
                return False
            
#######################################################
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal =i
                print(i,goal)
        return True if goal==0 else False