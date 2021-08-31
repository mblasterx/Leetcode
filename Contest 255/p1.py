class Solution(object):
    def findGCD(self, nums):
        maximum = max(nums)
        minimum = min(nums)
        while maximum * minimum > 0:
            temp = minimum
            minimum = maximum%minimum
            maximum = temp 
        return maximum+minimum

# s = Solution()
# print(s.findGCD([6,4,5,16]))