class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        word = nums[0]
        for i in range(len(nums)):
            if word[i] == '0':
                flip = '1'
            else:
                flip = '0'
            replacement = nums[0][:i] + flip + nums[0][i+1:]
            if replacement not in nums:
                return replacement


# s = Solution()
# print(s.findDifferentBinaryString(["111", "011", "001"]))