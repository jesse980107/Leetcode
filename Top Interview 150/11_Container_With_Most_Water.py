#Medium
#Two Pointers

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height)-1
        max_v=0
        while l <r:
            h = min(height[l],height[r])
            v= h* (r-l)
            max_v = max(max_v,v)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_v
