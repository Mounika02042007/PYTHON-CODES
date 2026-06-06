class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        leftSum = 0
        ans = []
        for num in nums:
            total -= num
            ans.append(abs(leftSum - total))
            leftSum += num
        return ans
