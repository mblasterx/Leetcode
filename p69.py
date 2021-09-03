class Solution:
    '''https://leetcode.com/problems/sqrtx/
    '''
    def mySqrt(self, x: int) -> int:
        '''Given a non-negative integer x, compute and return the square root of x.
        Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
        '''
        i = 1
        while i*i <= x:
            i+=1
        return i-1

    def test(self) -> None:
        testCases = {
            4       :2,
            1       :1,
            8       :2,
            15      :3,
            9       :3,
            0       :0,
        }
        for key,val in testCases.items():
            assert self.mySqrt(key) == val 
        print('All tests passed')
    
s = Solution()
s.test()