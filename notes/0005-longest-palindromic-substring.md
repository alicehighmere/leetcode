# 5. Longest Palindromic Substring

## Solution 1: Expand Around Centre

```python
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
```

### Approach

1. **Initialise the longest palindrome**
   - Use `pal_len` to store the longest length found.
   - Use `pal_idx` to store its starting index.
   - Initialise both variables before iterating through the string.

2. **Check both types of centre**
   - Visit each index using `range(len(s))`.
   - Start with `left = right = i` for odd-length palindromes.
   - Start with `left = i` and `right = i + 1` for even-length palindromes.
   - Check both cases at every position, regardless of the length of the input string.

3. **Expand while the characters match**
   - Check that both pointers are within bounds before accessing the string.
   - Compare `s[left]` and `s[right]`.
   - Move `left` backwards and `right` forwards while the characters match.

4. **Update the longest palindrome**
   - After expansion, both pointers are immediately outside the valid palindrome.
   - Calculate its length using `right - left - 1`.
   - If it is longer than the previous result, update both `pal_len` and `pal_idx`.
   - Use `left + 1` as the starting index.

5. **Return the substring**
   - Extract the result using `s[pal_idx:pal_idx + pal_len]`.

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(n²) | O(n) possible centres, each requiring up to O(n) expansion |
| SC | O(1) | Constant auxiliary space, excluding the returned substring |
| Runtime | 216 ms |  |
| Memory | 19.2 MB |  |

Python slicing creates the returned string, requiring O(k) space for a result of length k.

### Insights

- **Centre-Based Expansion:** Every palindrome has either a single-character centre or a centre between two adjacent characters. Checking both types covers all possible palindromic substrings.
- **Independent Parity:** The length of the input does not determine the length of its longest palindrome. For example, `abac` has an even length, but its longest palindrome, `aba`, has an odd length.
- **Indices and Characters:** `left` and `right` represent positions. Palindrome validation requires comparing `s[left]` and `s[right]`, rather than comparing the indices themselves.
- **Short-Circuit Evaluation:** Python evaluates `and` conditions from left to right. Checking bounds first prevents invalid access. Explicitly checking `left >= 0` also prevents negative indexing from reading characters at the end of the string.
- **Expansion Boundaries:** After the loop terminates, the valid palindrome extends from `left + 1` to `right - 1`. Its length is therefore `right - left - 1`.
- **Consistent Result Tracking:** The longest length and its starting index must be updated together, and only when a longer palindrome is found. Unconditional updates can overwrite an earlier result or associate its length with the wrong position.
- **Tie Handling:** Using `cur_len > pal_len` preserves the first longest palindrome found when multiple results have the same length.