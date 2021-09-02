class Solution:
    '''https://leetcode.com/problems/fibonacci-number/
    '''
    def fib(self, n: int) -> int:
        '''Returns the n-th fibonacci number
        '''
        if n == 0:
            return 0
            
        fibList = [0 for _ in range(n+1)] # base case, build cache with n+1 values since we start at F(0)->F(n) inclusive
        fibList[1] = 1

        j = 2
        while j<=n:
            fibList[j] = fibList[j-1] + fibList[j-2] # DP recurrence
            j+=1
        return fibList[n]

    def test(self) -> None:
        testCases = {
            0               :0,
            2               :1,
            3               :2,
            5               :5,
            7               :13,
        }
        for key,val in testCases.items():
            assert self.fib(key) == val 
        print('All tests passed')
    
s = Solution()
s.test()