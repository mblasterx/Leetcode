from typing import List
class Solution:
    '''https://leetcode.com/problems/remove-duplicates-from-sorted-array/
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        '''
        if len(nums) == 0:
            return 0

        numDiff = 1
        curMaxValue = nums[0]
        '''
        The key is that we will know where the k-th number in increasing order lies in the new array, so we keep track of where its supposed to be an randomly swap everything else around
        Time: O(n), memory O(1)
        '''
        for i in range(0,len(nums)):
            if nums[i] != curMaxValue:
                if i != numDiff: # we have a new value on a bad position, swap it with the one at the numDiff position 
                    nums[numDiff] = nums[i]
                    nums[i] = curMaxValue
                curMaxValue = nums[numDiff]
                numDiff += 1
            # if they are equal nothing happens we move on   
        return numDiff 

    def test(self) -> None:
        testCases = {
            "1,1,2"                 :2,     #[1,2]
            "0,0,1,1,1,2,2,3,3,4"   :5,     #[0,1,2,3,4]
            "1,2"                   :2,     #[1,2]
        }

        for key,val in testCases.items():
            assert self.removeDuplicates(key.split(',') ) == val    # input has to be a list
        print('All tests passed')
    
s = Solution()
s.test()