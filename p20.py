class Solution:
    def isValid(self, s: str) -> bool:
        '''https://leetcode.com/problems/valid-parentheses/
        '''
        while True:
            curLenS = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            if curLenS == len(s):
                break
        return len(s) == 0

    def test(self) -> None:
        testCases = {"()":True, "()[]{}":True, "(]":False, "([)]":False, "{[]}":True}
        for key,val in testCases.items():
            assert self.isValid(key) == val 
        print('All tests passed')
    
s = Solution()
s.test()   