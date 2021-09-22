class Solution:
    '''https://leetcode.com/problems/divide-two-integers/
    '''
    def divide(self, dividend: int, divisor: int) -> int:
        '''Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
        Return the quotient after dividing dividend by divisor.
        '''
        
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

    def test(self) -> None:
        testCases = {
            (10,3)              :3,
            (7,-3)              :-2,
            (0,1)               :0,
            (1,1)               :1,
            (-2147483648, -1)   :2147483647,
        }
        for (divident, divisor),val in testCases.items():
            assert self.divide(divident, divisor) == val 
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()