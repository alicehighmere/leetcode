# 1. Two Sum

## Solution 1: Brute Force
```Python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for index, num in enumerate(nums):
            comp = target - num

            for index_slice, num in enumerate(nums[index+1:]):
                if comp == num:
                    index_match = index + 1 + index_slice

                    return [index, index_match]
```

### Approach
1. Iterate through the array using nested loops.
    - Use **enumerate()** to access each element’s index and value.
    - Start the inner loop at index + 1 to avoid duplicate pairs.
    - Check each pair only once.
2. Calculate and search for the complement.
    - Calculate `target - num` to find the required value.
    - Search the remaining elements for the complement.
    - Use the inner loop to check each candidate.
3. Return the matching indices.
    - Check whether the current value matches the complement.
    - Calculate the matching index using the slice offset.
    - Return both indices immediately when a match is found.

### Analysis
| Metric | Value | Comment |
|:---:|:---:|---|
| TC | O(n<sup>2</sup>) | Nested loops may examine every pair in the worst case |
| SC | O(n) | List slicing creates temporary lists proportional to the input size |
| Runtime | 1210 ms |
| Memory | 19.72 MB |

### Insights
- **enumerate()**: Iterates over index-value pairs
- List Slicing: Creates a new list
- Nested Loops: Can result in O(n²) time complexity
- Early return: Stops execution once a match is found


## Solution 2: Hash Table
```Python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            comp = target - num
            
            if comp in seen:
                return [seen[comp], index]
            
            else:
                seen[num] = index
```

### Approach
1. Initialize a **hash table**.
    - Use a **dictionary** (seen) to store previously visited values and their indices.
    - Map each number to its index.
2. Calculate and search for the complement.
    - Calculate `target - num` to find the required value.
    - Check whether the complement exists in seen.
    - Dictionary lookups take O(1) time on average.
3. Return the matching indices or store the current element.
    - If the complement exists, return its stored index and the current index.
    - Otherwise, store the current number and its index.
    - Check before inserting to avoid reusing the same element.

### Analysis
| Metric | Value | Comment |
|:---:|:---:|---|
| TC | O(n) | One pass with O(1) average dictionary operations |
| SC | O(n) | The dictionary may store up to n elements |
| Runtime | 1 ms |
| Memory | 20.48 MB |

### Insights
- **Dictionary**: Stores key-value pairs for efficient lookups
- **in**: Checks whether a key exists in a dictionary
- **Hash table**: Provides O(1) average-time insertion and lookup
- Check before insert: Handles duplicate values without reusing the same index