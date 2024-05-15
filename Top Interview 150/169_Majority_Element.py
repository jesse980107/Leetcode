import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {i: 0 for i in nums}
        half_length = len(nums) / 2

        for i in nums:
            map[i] += 1

            if map[i] > half_length:
                return i
##########################

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {i: 0 for i in nums}
        half_length = len(nums) / 2

        for i in nums:
            map[i] += 1

            if map[i] > half_length:
                return i
