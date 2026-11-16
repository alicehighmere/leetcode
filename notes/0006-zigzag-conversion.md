# 6. Zigzag Conversion

## Solution 1: Row-by-Row Simulation

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        rows = [''] * numRows
        row = 0
        direction = 1

        # prevent invalid row movement when only one row is required
        if numRows == 1:
            return s

        for i in range (len(s)):

            rows[row] += s[i]

            if row == 0:
                direction = 1

            # use elif to make only one direction change occurs at a time
            elif row == numRows - 1:
                direction = -1

            row += direction
        
        return ''.join(rows)
```

### Approach

1. **Handle the edge case**
   - Return the original string when `numRows == 1`
   - This prevents invalid row movement

2. **Initialise rows and direction**
   - Create `numRows` empty strings to represent individual rows
   - Initialise `row = 0` and `direction = 1`

3. **Distribute characters**
   - Append each character to the current row
   - Set `direction = 1` at the first row and `-1` at the last row
   - Update the current row using `row += direction`

4. **Construct the result**
   - Concatenate all row strings using `''.join(rows)`
   - Return the converted string

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(n) | Each character is processed once |
| SC | O(n) | Stores characters across row strings |
| Runtime | 13 ms | |
| Memory | 19.37 MB | |

### Insights

**1. Zigzag Cycle**

- Each cycle contains `numRows` downward characters and `numRows - 2` upward characters
- Cycle Length: `2 * (numRows - 1)`
- Tracking row indices and direction avoids constructing a two-dimensional matrix

**2. List Initialisation**

```python
rows = [''] * numRows
```

- Creates a list containing `numRows` empty strings
- Avoid `[[]] * n` for independent nested lists
    - It creates shared references
    - Use `[[] for _ in range(n)]` instead

**3. String Joining**

```python
''.join(rows)     # Concatenates without a separator
' '.join(words)   # Concatenates with spaces
```

- `join()` combines an iterable of strings using the preceding string as a separator
- All elements must be strings

**4. Conditional Branching**

- `if` + `if` evaluates conditions independently
- `if` + `elif` ensures only one branch executes
- `elif` expresses mutually exclusive direction changes more clearly