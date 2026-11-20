# 195. Tenth Line

## Solution 1: `sed`

```bash
sed -n '10p' file.txt
```

### Approach

- `sed` (Stream Editor) processes text line by line
- `-n` suppresses automatic output
- `10p` prints only the 10th line
- Produces no output if the file contains fewer than 10 lines

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(n) | Reads up to 10 lines, independent of total file length |
| SC | O(1) | Processes lines without storing the entire file |
| Runtime | 11 ms | |
| Memory | 3.82 MB | |

### Insights

- `sed` is useful for selecting, editing, and replacing text
- Without `-n`, `sed '10p'` prints every line and duplicates the 10th line
- `sed -n '5,10p'` prints lines 5 through 10

## Solution 2: `awk`

```bash
awk 'NR == 10 {print}' file.txt
```

### Approach

- `awk` processes text using pattern-action rules
- `NR` (Number of Records) tracks the current record number
- `NR == 10` selects the 10th line
- `{print}` outputs the selected line

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(n) | Checks the record number for each line |
| SC | O(1) | Processes one record at a time |
| Runtime | 10 ms | |
| Memory | 3.8 MB | |

### Insights

- `NR` counts records across all input files
- `FNR` counts records separately for each input file
- `awk 'NR == 10' file.txt` also works because matching records are printed by default

## Solution 3: `tail` | `head`

```bash
tail -n +10 file.txt | head -n 1
```

### Approach

- `tail -n +10` extracts all lines starting from the 10th line
- `|` passes the output to the next command
- `head -n 1` selects the first line from that output
- Produces no output if the file contains fewer than 10 lines

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(n) | Reads the input from the 10th line onwards |
| SC | O(1) | Processes a stream without storing the entire file |
| Runtime | 22 ms | |
| Memory | 3.9 MB | |

### Insights

- `head -n N` selects the first N lines
- `tail -n N` selects the last N lines, whereas `tail -n +N` starts from line N
- The initial `head -n 10 | tail -n 1` approach incorrectly outputs the last available line when the file contains fewer than 10 lines
- Reversing the pipeline with `tail -n +10 | head -n 1` handles this edge case correctly