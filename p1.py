from typing import List
class Solution:
    '''https://leetcode.com/problems/two-sum/
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Simple check all algorithm O(n^2)
        '''
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target: return [i,j]

    def test(self) -> None:
        # use pop method to extract target
        # 2 <= nums.length <= 104
        # -109 <= nums[i] <= 109
        # -109 <= target <= 109
        testCases = [
            ([2,7,11,15],   9,  [0,1]),
            ([3,2,4],       6,  [1,2]),
            ([3,3],         6,  [0,1]),
        ]
        
        for (nums, target, expectedResult) in testCases:
            assert self.twoSum(nums,target) == expectedResult, (nums, target, self.twoSum(nums,target), expectedResult)
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main() 