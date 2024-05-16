#Medium
#Two Pointers

#this is not good since it's O(n^2)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        star = 0
        curr = 0
        while star < len(numbers)-1:
            sub = target-numbers[star]
            for i in range(star+1,len(numbers)):
                if numbers[i] == sub and star!= i:
                    return [star+1,i+1] 
            star+=1
##############################################
#hash map/dictionary  approach 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in index_map:
                return [index_map[complement] + 1, i + 1]  # Return indices as 1-based
            index_map[num] = i  # Store the index of each element
##############################################
# two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while r>l:
            if numbers[l]+numbers[r] > target:
                r-=1
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]

  