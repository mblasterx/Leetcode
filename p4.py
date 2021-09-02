class Solution(object):
    '''https://leetcode.com/problems/median-of-two-sorted-arrays/
    '''
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """:type nums1: List[int]
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

    def test(self) -> None:
        # If we need to compare floats use 
        # from math import isclose

        testCases = {
            ("1,2", "3,4")  :2.5,
            ("1,3", "2")    :2.0,
            ("0,0", "0,0")  :0.0,
            ("", "1")       :1.0,
            ("2", "")       :2.0,
        }

        for (key1, key2),val in testCases.items():
            # first turn the test strings into proper inputs in our problem function
            nums1 = list(map(int, key1.replace(',', '')))   
            nums2 = list(map(int, key2.replace(',', '')))

            assert self.findMedianSortedArrays(nums1, nums2) == val 
        print('All tests passed')


s = Solution()
s.test()