# 7. Reverse Integer

## Solution 1: Arithmetic Reversal

```python
class Solution:
    def reverse(self, x: int) -> int:
        
        rvs = 0
        sgn = 1

        if x < 0:
            sgn = -1
            x = -x

        MAX = (2 ** 31) - 1 if sgn == 1 else (2 ** 31)

        while x > 0:
            dgt = x % 10

            if rvs > MAX // 10 or (rvs == MAX and dgt > MAX % 10):
                return 0

            rvs = (rvs * 10) + dgt
            x = x // 10
        
        return sgn * rvs
```

### Approach

1. **Separate the sign**
   - Store the sign in `sgn` and convert negative inputs to positive values
   - Define the 32-bit limit according to the original sign

2. **Reverse the digits**
   - Extract the last digit using `x % 10`
   - Append it using `rvs = rvs * 10 + digit`
   - Remove the processed digit using `x // 10`
   - Repeat until `x` becomes `0`

3. **Prevent overflow**
   - Check whether appending the next digit would exceed the 32-bit limit
   - Return `0` if overflow is detected
   - Otherwise, return the reversed integer with its original sign

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(log n) | Processes each decimal digit once |
| SC | O(1) | Uses a fixed number of variables |
| Runtime | 1 ms | |
| Memory | 19.18 MB | |

### Insights

- **Digit manipulation:** `% 10` extracts the last digit, while `// 10` removes it
- **Integer construction:** `rvs * 10 + digit` appends a digit without string conversion
- **Signed 32-bit range:** `-2**31` to `2**31 - 1`, with different absolute limits for positive and negative values
- **Overflow prevention:** Check the result before multiplying by 10 and appending the next digit

  ```python
  if rvs > LIMIT // 10 or (rvs == LIMIT // 10 and digit > LIMIT % 10):
      return 0
  ```

  - `rvs > LIMIT // 10`: Multiplication by 10 would exceed the limit
  - `rvs == LIMIT // 10`: The next digit must not exceed `LIMIT % 10`
  - For the positive limit `2147483647`, a prefix of `214748364` can only accept a final digit of `7` or less
  - This prevents overflow without requiring a 64-bit intermediate integer
