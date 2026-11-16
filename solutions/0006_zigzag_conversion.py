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