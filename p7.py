class Solution:
    '''https://leetcode.com/problems/reverse-integer/
    '''
    def reverse(self, x: int) -> int:
        '''
        version 1 make into string, then reverse 
        '''
        sign = -1 if x < 0 else 1   # remember the sign
        x *= sign # make x positive
        res = sign*int(str(x)[::-1]) # reverse the string with slicing 
        if res not in range(-2**31, 2**31-1): # check for out of range
            return 0
        return res

    def test(self) -> None:
        testCases = {
            123     :321,
            -123    :-321,
            120     :21,
            0       :0,
        }
        for key,val in testCases.items():
            assert self.reverse(key) == val 
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()