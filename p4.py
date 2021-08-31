# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        nums = nums1+nums2
        nums.sort()
        totalNums = len(nums)
        if totalNums%2 == 0:
            return float((nums[totalNums//2] + nums[totalNums//2-1])/2)
        else:
            return float(nums[totalNums//2])



        
from math import isclose

s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1, nums2))
# print(isclose(s.findMedianSortedArrays(nums1, nums2), output))