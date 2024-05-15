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
        if len(nums) == 1:
            return True
        
        N = len(nums)
        # print(N)

        gas = 0
        for index, n in enumerate(nums):
            # print(gas, n, index)
            gas = max(gas - 1, n)
            # print(gas)


            if gas >= (N - (index + 1)):
                # print('early exit')
                return True

            if gas <= 0:
                return False

        return True