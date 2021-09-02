class Solution:
    '''https://leetcode.com/problems/palindrome-number/
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
    '''
    def isPalindrome(self, x: int) -> bool:
        return x == self.reverse_number(x)

    def reverse_number(self, x:int) -> int:
        palindrome = 0
        while x>0:
            palindrome = palindrome*10 + x%10
            x = x//10     
        return palindrome

    def test(self) -> None:
        testCases = {
            123     :False,
            1221    :True,
            12321   :True,
            0       :True,
        }
        for key,val in testCases.items():
            assert self.isPalindrome(key) == val 
        print('All tests passed')
    
s = Solution()
s.test()      
        