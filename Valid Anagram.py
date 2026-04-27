class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=sorted(t)
        y=sorted(s)
        if(len(x)!=len(y)):
            return False
        i=0
        while(i<len(s)):
            if(x[i]!=y[i]):
                return False
            i+=1
        return True
        
