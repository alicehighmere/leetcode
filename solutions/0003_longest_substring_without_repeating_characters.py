class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        d = {}
        max_len = 0

        for right in range (len(s)):
        
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1

            d[s[right]] = right
            max_len = max(max_len, right - left + 1)


        return max_len