# 193. Valid Phone Numbers

## Solution 1: Extended Regular Expressions with `grep`

```bash
grep -E '(^[0-9]{3}-[0-9]{3}-[0-9]{4}$)|(^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$)' file.txt
```

### Approach

1. Use `grep` to search `file.txt` and print lines matching the specified patterns.
2. Use `-E` to enable Extended Regular Expressions (ERE), which support repetition counts and alternation without additional escaping.
3. Define the two valid phone number formats as separate patterns:
   - `[0-9]{3}-[0-9]{3}-[0-9]{4}` matches `xxx-xxx-xxxx`.
   - `\([0-9]{3}\) [0-9]{3}-[0-9]{4}` matches `(xxx) xxx-xxxx`.
4. Use `^` and `$` to ensure each pattern matches the entire line.
5. Connect the patterns with `|` to match either format.

### Analysis

| Metric | Value | Comment |
|---|---|---|
| Time Complexity | O(n) | Each line is checked against the regular expression. `n` represents the total input size. |
| Space Complexity | O(1) | No additional data structure is explicitly created; auxiliary space is considered, excluding output buffering and implementation details. |

### Insights

- **`grep`** searches text for lines matching a pattern and prints the matching lines.
- **`-E`** enables Extended Regular Expressions, supporting `{n}` repetition and `|` alternation.
- **`[0-9]{n}`** matches exactly `n` consecutive digits.
- **`^` and `$`** anchor a pattern to the beginning and end of a line, preventing partial matches.
- **`\(` and `\)`** match literal parentheses rather than using them as grouping operators.
- **`|`** represents OR within a regular expression. It differs from the Bash pipe operator, which passes one command's output to another command.
- **Single quotes (`'...'`)** prevent Bash from interpreting the pattern's special characters before `grep` receives it.