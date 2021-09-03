class Solution:
    '''https://leetcode.com/problems/sqrtx/
    '''
    def mySqrt(self, x: int) -> int:
        '''Simple linear search
        '''
        i = 1
        while i*i <= x:
            i+=1
        return i-1

    def mySqrt(self, x: int) -> int:
        '''Divide and conquer
        '''
        if x <= 1: 
            return x
        
        left, right = 1, x // 2 + 1
        while left < right:
            mid = (left + right) // 2   # adjust the window
            square = mid * mid         
            # we check for squares, or move the window and shrink it in half
            if square == x:     
                return mid
            if square > x: 
                right = mid
            else: 
                left = mid + 1
        
        return right - 1

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