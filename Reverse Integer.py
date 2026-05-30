class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        n = abs(x)
        rev = 0
        while n > 0:
            rem = n % 10
            rev = (rev * 10) + rem
            n = n // 10
        rev = sign * rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
