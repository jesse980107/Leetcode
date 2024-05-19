#Medium
#Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        distinct_set = set()

        for i, ele in enumerate(s):
            while ele in distinct_set:
                distinct_set.remove(s[l])
                l += 1
            w = i - l + 1
            longest = max(longest, w)
            distinct_set.add(ele)

        return longest


