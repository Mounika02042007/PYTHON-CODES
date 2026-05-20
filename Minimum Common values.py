class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x=0
        y=0
        while(x<len(nums1) and y<len(nums2)):
            if(nums1[x]==nums2[y]):
               return nums1[x]
            elif(nums1[x]<nums2[y]):
                x+=1
            else:
                y+=1
        return -1
