class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        Max = 1
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count > Max:
                Max = count
                ans = nums[i]
        return ans
