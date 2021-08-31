class Solution:
    def fib(self, n: int) -> int:
        '''https://leetcode.com/problems/fibonacci-number/
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
        inputs = [0,2,3,4 ,5, 6,7]
        outputs = [0, 1,2,3, 5, 8, 13]
        for input, output in zip(inputs, outputs):
            print(input, self.fib(input), output)

s = Solution()
s.test()