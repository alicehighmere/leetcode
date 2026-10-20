class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cur_len = 0
        max_len = 0
        
        for i in range(len(s)):
            d = {}
            
            for j in range(i, len(s)):
                if s[j] in d:
                    cur_len = len(d)
                    max_len = max(max_len, cur_len)
                    break

                else:
                    d[s[j]] = j
                    cur_len = len(d)
                    max_len = max(max_len, cur_len)


        return max_len