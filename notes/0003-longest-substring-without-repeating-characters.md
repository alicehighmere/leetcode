# 3. Longest Substring Without Repeating Characters

## Solution 1: Brute Force with Dictionary

```Python
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
```

### Approach

1. Initialise variables
    - `cur_len`: Length of the current substring without repeating characters.
    - `max_len`: Maximum length found so far.
    - `d`: Dictionary storing each character and its index in the current substring.

2. Choose a starting position
    - Use the outer loop to iterate through every index in `s`.
    - Initialise an empty dictionary for each starting position.
    - Each iteration explores substrings starting at a different index.

3. Expand the substring
    - Use the inner loop to traverse characters from the current starting position.
    - If the character is not in `d`, add it as a key and store its index as the value.
    - Update `cur_len` using `len(d)` and update `max_len` accordingly.
    - If the character already exists in `d`, stop the current search with break.

4. Return the maximum length
    - Repeat the search for every possible starting position.
    - Return `max_len` after all starting positions have been examined.

### Analysis

| Metric | Value | Comment |
|:---:|:---:|---|
| TC | O(n<sup>2</sup>) | The nested loops may examine O(n²) characters in total |
| SC | O(min(n, Σ)) | The dictionary stores distinct characters in the current substring, where Σ is the character set size |
| Runtime | 3498 ms |
| Memory | 19.82 MB |

### Insights

- **Brute Force**: Enumerate every possible starting position and expand the substring until a duplicate character appears.
- Dictionary for Duplicate Detection: A dictionary supports efficient average-case membership checks with `if s[j] in d`. Storing indices also preserves the positions of previously encountered characters.
- Nested Loops: The outer loop selects the starting position, while the inner loop expands the substring. Separating these responsibilities makes the search strategy explicit.
- Early Termination with break: Once a duplicate appears, extending the current substring cannot produce a valid substring from the same starting position. Stop the inner loop and move to the next starting position.
- Tracking the Maximum: Use `max(max_len, cur_len)` to preserve the longest valid substring found across all starting positions.
- Substring vs. Subsequence: A substring must consist of consecutive characters. For example, "kew" is a valid substring of "pwwkew", whereas "pwe" is not.
- Optimisation Opportunity: Different starting positions can cause repeated character checks. A more efficient approach can avoid this redundant work.

## Solution 2: Sliding Window

```Python
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
```

### Approach

1. Initialise variables
    - `left`: starting index of the current valid window.
    - `right`: index of the character currently being examined.
    - `d`: dictionary mapping each character to its most recent index.
    - `max_len`: length of the longest valid substring found so far.
2. Detect duplicates
    - Iterate through the string using right.
    - Check whether `s[right]` exists in `d` and its last-seen index is greater than or equal to left.
    - If both conditions are true, the character is duplicated within the current window.
    - Move `left` to `d[s[right]] + 1`, excluding the previous occurrence and all characters before it.
3. Update the window
    - Store the current index with `d[s[right]] = right`.
    - Calculate the current window length using `right - left + 1`.
    - Update `max_len` with the larger of the current length and the previous maximum.
4. Return the result
    - Return `max_len` after the entire string has been examined.
    - An empty string returns 0 without entering the loop.

### Analysis

| Metric | Value | Comment |
|:---:|:---:|---|
| TC | O(n) | Each character is examined once – `left` only moves forwards |
| SC | O(min(n, Σ)) | The dictionary stores at most one entry per distinct character, where Σ is the character set size |
| Runtime | 192 ms |
| Memory | 19.86 MB |

### Insights

- **Sliding Window**: Maintains a valid substring without restarting the search after finding a duplicate.
- Last-seen Index: The dictionary stores each character’s most recent index, allowing left to jump directly past a duplicate.
- Window Boundary: A previous occurrence is relevant only when its index is greater than or equal to left. Older occurrences outside the current window must be ignored.
- Monotonic Pointer: left never moves backwards, preventing unnecessary re-examination of characters.
- Efficiency: Improves on the Brute Force solution’s O(n²) time complexity by reusing information from previous iterations.