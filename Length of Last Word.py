class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis=list(map(str,s.split()))
        x=lis[-1]
        return len(x)
