class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        intNums = [int(x) for x in nums]
        intNums.sort()

        for i in range(k):
            reslt = intNums.pop()
    
        return str(reslt)

# s = Solution()
# test = ["3","6","7","10"]
# k = 4
# print(s.kthLargestNumber(test,k))