'''
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, assume that your function returns 2^31 − 1 when the division result overflows.    
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # deal with end cases -2^31 in, 2^31 not in
        if dividend == -2147483648:
            if divisor == 1:
                return dividend
            elif divisor == -1:
                return abs(dividend+1)

        # check for the sign first, do both positive operation              
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0): # if only one is negative
            return -self.divide(abs(dividend), abs(divisor))
        dividend, divisor = abs(dividend), abs(divisor) # make them both positive

        if divisor == 1:
            if dividend > 2147483647: # deal with end cases -2^31 in, 2^31 not in
                return dividend - 1
            else:
                return dividend
                
        if dividend < divisor: 
            return 0

        power = divisor
        quotient = 1
        while dividend>=power+power:
            quotient += quotient
            power += power
        return quotient+self.divide(dividend-power, divisor)

s = Solution()
print(s.divide(-2147483648, -1))