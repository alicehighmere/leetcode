# 194. Transpose File

## Solution 1: AWK Array

```bash
awk '{for (i=1; i<=NF; i++) if (NR==1) {arr[i] = $i} else {arr[i] = arr[i] " " $i}} END {for (i=1; i<=NF; i++) print arr[i]}' file.txt
```

### Approach

1. **Read and split each line**
   - AWK processes the file line by line
   - `NF` represents the number of fields in the current line
   - `$i` accesses the i-th field

2. **Build the transposed rows**
   - Use an associative array `arr[i]` to store each column
   - For the first line (`NR == 1`), initialise each array element
   - For subsequent lines, append each field with a separating space

3. **Print the transposed file**
   - `END` executes after all input lines have been processed
   - Iterate through the array indices and print each transposed row
   - The solution assumes every input line has the same number of fields

### Analysis

| Metric | Value | Comment |
|---|---|---|
| TC | O(R × C) | Processes every field; excludes potential additional string concatenation costs |
| SC | O(R × C) | Stores the transposed content in an array |
| Runtime | 35 ms | |
| Memory | 3.82 MB | |

- `R`: Number of input rows
- `C`: Number of input columns

### Insights

**1. Shell quoting and AWK syntax**

```bash
awk '{print $1}' file.txt
```

| Syntax | Role | Explanation |
|---|---|---|
| `awk` | Shell command | Executes an AWK programme |
| `'...'` | Shell quoting | Prevents Shell expansion of special characters such as `$1` |
| `{...}` | AWK action block | Contains statements executed for matching records |
| `print $1` | AWK statement | Prints the first field of the current record |
| `file.txt` | Input | Specifies the file to process |

- Single quotes belong to Shell syntax, while curly braces belong to AWK syntax
- AWK follows the `pattern { action }` structure
- Omitting `pattern` executes the action for every input record
- AWK programmes can span multiple lines inside Shell quotes

**2. AWK variables and arrays**

| Syntax | Description |
|---|---|
| `NR` | Number of Records processed so far |
| `NF` | Number of Fields in the current record |
| `$i` | Value of the i-th field |
| `arr[i]` | Associative array element indexed by `i` |
| `arr[i] = $i` | Assign a field to an array element |
| `arr[i] = arr[i] " " $i` | Append a field with a separating space |

- AWK arrays are associative and require no explicit declaration
- Adjacent expressions perform string concatenation without a dedicated operator
- Numeric `for` loops preserve the intended output order, unlike `for (i in arr)`

**3. AWK execution blocks**

| Block | Execution |
|---|---|
| `BEGIN { ... }` | Once before processing input |
| `{ ... }` | Once for each input record |
| `END { ... }` | Once after processing all input |

- AWK supports C-style `for` loops and `if...else` statements
- `END` is useful for printing accumulated results
- `NF` in `END` retains the last input record's field count

**4. Shell output redirection**

- `>` redirects standard output to a file, truncating it before the command executes
- Never use the same file as both input and redirected output
- LeetCode expects standard output, so no redirection is required
