class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        l = str(n)
        x = str(x)
        if l[0] == x:
            return False
        if x in l:
            return True
        return False
