class Solution:
    def minElement(self, nums: List[int]) -> int:
        lis = []
        for i in nums:
            Sum = 0
            j = str(i)
            for k in j:
                Sum += int(k)
            lis.append(Sum)
        return min(lis)
