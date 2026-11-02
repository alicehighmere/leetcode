# 4. Median of Two Sorted Arrays

## Solution 1: Binary Search (Partition-Based)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Search the shorter array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        full = m + n

        # Number of elements in the left partition.
        half = (full + 1) // 2

        left = 0
        right = m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half - cut1

            # Handle empty partition boundaries.
            left_max_num1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            left_max_num2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            right_min_num1 = nums1[cut1] if cut1 < m else float('inf')
            right_min_num2 = nums2[cut2] if cut2 < n else float('inf')

            # Check for a valid partition.
            if left_max_num1 <= right_min_num2 and left_max_num2 <= right_min_num1:
                if full % 2 == 1:
                    return max(left_max_num1, left_max_num2)
                else:
                    return (max(left_max_num1, left_max_num2) + min(right_min_num1, right_min_num2)) / 2

            # Move the partition left.
            elif left_max_num1 > right_min_num2:
                right = cut1 - 1

            # Move the partition right.
            elif left_max_num2 > right_min_num1:
                left = cut1 + 1
```

### Approach

1. **Select the shorter array**
   - Swap the arrays if `nums1` is longer than `nums2`.
   - Minimise the binary search space.
   - Keep the corresponding partition of `nums2` within valid bounds.

2. **Determine the partition sizes**
   - Calculate the total number of elements.
   - Use `half = (full + 1) // 2` to determine the left partition size.
   - Include the median in the left partition when the total is odd.
   - Maintain `cut1 + cut2 = half`.

3. **Find the partition boundaries**
   - Apply binary search to the partition positions of `nums1`.
   - Calculate `cut1` from the current search boundaries.
   - Derive `cut2` from the remaining elements required.
   - Identify the largest left-side and smallest right-side elements in both arrays.
   - Use negative and positive infinity for empty partition boundaries.

4. **Validate and adjust the partition**
   - A valid partition requires `left_max_num1 <= right_min_num2` and `left_max_num2 <= right_min_num1`.
   - If `left_max_num1 > right_min_num2`, move `cut1` left.
   - If `left_max_num2 > right_min_num1`, move `cut1` right.
   - Update the binary search boundaries to eliminate invalid candidates.

5. **Calculate the median**
   - For an odd total, return the maximum element of the left partition.
   - For an even total, return the average of the left maximum and right minimum.

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(log(min(m, n) + 1)) | Binary search on the shorter array |
| SC | O(1) | Constant additional space |
| Runtime | 2 ms |  |
| Memory | 19.40 MB |  |

### Insights

- **Binary Search:** Repeatedly eliminates approximately half of the remaining search candidates, producing logarithmic time complexity when each iteration takes constant time.
- **Partition-Based Search:** Searches for a valid partition position rather than a specific value. Both arrays remain separate throughout the algorithm.
- **Fixed Partition Size:** The total number of elements in the left partition remains constant. Increasing `cut1` decreases `cut2` by the same amount.
- **Boundary Validation:** Since both arrays are sorted, comparing only four boundary values is sufficient to verify the partition.
- **Sentinel Values:** `float('-inf')` and `float('inf')` represent missing boundary elements. They preserve valid comparisons without additional special cases.
- **Search Direction:** A left-side value exceeding the opposite right-side value determines which half of the partition candidates can be discarded.
- **Median Calculation:** An odd total uses the left maximum. An even total uses the average of the left maximum and right minimum.