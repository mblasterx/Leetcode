'''
https://leetcode.com/problems/climbing-stairs/
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        '''Returns the number of ways you can climb n stairs in increments of 1, 2
        Basically memoization of Fibonacci recurrence 
        '''
        if n in {0,1}: # base case
            return n
        memo = [1,1] +[0 for _ in range(2,n+1)] # set up the cache
        for i in range(2,n+1):  # recurrence
            memo[i] = memo[i-1] + memo[i-2]
        return memo[n]
        
# simple test
s = Solution()
n = 10
print(s.climbStairs(n))