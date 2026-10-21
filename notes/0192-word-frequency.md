# 192. Word Frequency

## Solution 1: Basic Pipeline

```bash
cat words.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```

### Insights

- `sort` processes complete lines, not individual words. Running `cat words.txt | sort` sorts the original lines, which may already be in order and therefore appear unchanged.
- `uniq -c` counts only consecutive identical lines. `sort` must come first to group identical words together.
- `sort -nr` sorts the frequency counts numerically in descending order.
- `awk '{print $2, $1}'` reverses the fields from `count word` to `word count`.

### Limitations

- `tr ' ' '\n'` replaces every space with a newline.
- Multiple consecutive spaces therefore produce empty lines.
- `uniq -c` counts these empty lines as well as actual words.

---

## Solution 2: Squeeze Repeated Spaces

```bash
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```

### Improvements

- `tr -s ' ' '\n'` squeezes consecutive spaces into a single space before translating them into newlines.
- This prevents multiple spaces between words from generating empty lines.

### Limitations

- `tr -s` does not remove leading or trailing spaces.
- A leading space can still produce an empty line, which `uniq -c` may count as a separate entry.
- The approach also handles ordinary spaces rather than treating all whitespace characters as field separators.

---

## Solution 3: Extract Fields with `awk`

```bash
awk '{for (i = 1; i <= NF; i++) print $i}' words.txt | sort | uniq -c | sort -nr | awk '{print $2, $1}'
```

### Improvements

- `awk` splits each line into fields using whitespace as the default field separator.
- `NF` provides the number of fields in the current line.
- The `for` loop prints each field separately, avoiding empty entries caused by leading, trailing, or repeated whitespace.
- The remaining pipeline groups identical words, counts their occurrences, sorts by frequency, and formats the final output.

### Insights

- `tr` transforms individual characters; `awk` can process structured fields.
- Choose the operation based on the input's structure and the edge cases that must be handled.
- Testing leading spaces, repeated spaces, and trailing spaces helps identify assumptions that a simpler pipeline may overlook.

### Analysis
| Metric | Value |
|:---:|:---:|
| Runtime | 52 ms |
| Memory | 3.65 MB |