# Read from the file file.txt and output the tenth line to stdout.

# Solution 1: sed
sed -n '10p' file.txt

# Solution 2: awk
awk 'NR == 10 {print}' file.txt

#Solution 3: tail | head
tail -n +10 file.txt | head -n 1