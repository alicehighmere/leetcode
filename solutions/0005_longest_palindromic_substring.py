class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        pal_len = 0
        pal_idx = 0 # start index

        for i in range (len(s)):

            # when the palindrome has an odd number of elements
            left, right = i, i
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            cur_len = right - left - 1

            if cur_len > pal_len:
                pal_len = cur_len
                pal_idx = left + 1

            # when the palindrome has an even number of elements
            left, right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            cur_len = right - left - 1
            
            if cur_len > pal_len:
                pal_len = max(pal_len, right - left - 1)
                pal_idx = left + 1
        
        return s[pal_idx:pal_idx + pal_len]