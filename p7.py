class Solution:
    def reverse(self, x: int) -> int:
        '''https://leetcode.com/problems/reverse-integer/
        version 1 make into string, then reverse 
        '''
        sign = -1 if x < 0 else 1   # remember the sign
        x *= sign # make x positive
        res = sign*int(str(x)[::-1]) # reverse the string with slicing 
        if res not in range(-2**31, 2**31-1): # check for out of range
            return 0
        return res

    def test(self) -> None:
        '''Testing some outputs'''
        inputs = [123, -123, 120, 0]
        outputs = [321, -321, 21, 0]
        for input, output in zip(inputs,outputs):
            print(input, self.reverse(input) , output)


s = Solution()
s.test()