class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            x=[]
            while i>0:
                x.append(i%10)
                i=i//10
            res.extend(x[::-1])
        return res
