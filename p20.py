class Solution:
    def isValid(self, s: str) -> bool:
        '''https://leetcode.com/problems/valid-parentheses/
        '''
        while True:
            curLength = len(s)
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            if curLength == len(s):
                break
        return len(s) == 0

    def isValid(self, s: str) -> bool:
        '''Nice stack solution
        '''
        match = dict(['()', '{}', '[]'])
        stack = []
        
        for char in s:
            if len(stack) and match.get(stack[-1], None) == char:
                stack.pop()
            else:
                stack.append(char)
        return not len(stack)

    def test(self) -> None:
        testCases = {
            "()":True, 
            "()[]{}":True, 
            "(]":False, 
            "([)]":False, 
            "{[]}":True
        }
        for key,val in testCases.items():
            assert self.isValid(key) == val 
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()