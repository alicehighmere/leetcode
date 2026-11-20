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