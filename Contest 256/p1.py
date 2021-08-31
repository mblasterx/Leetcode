class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        n = len(nums)
        diffs = [ [] for _ in range(n)]
        uniqueDiffs = []
        for i in range(n):
            for j in range(n):
                currentDiff = abs(nums[i]-nums[j])
                diffs[i].append(currentDiff)
                if currentDiff not in uniqueDiffs:
                    uniqueDiffs.append(currentDiff)
        uniqueDiffs.sort(reverse=True)
        
        if k == 2:
            return uniqueDiffs[0]
        
        while len(uniqueDiffs) > 0:
            currentDiff = uniqueDiffs.pop()
            
        
        return 0
        
s = Solution()
test = [9,4,1,7]
k = 3
print(s.minimumDifference(test,k)==5)