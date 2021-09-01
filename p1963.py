class Solution:
    def minSwaps(self, s: str) -> int:
        '''https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
        '''
        maxClosing = 0
        extraClosingBrackets = 0
        for char in s:
            if char == ']':
                extraClosingBrackets += 1
                maxClosing = max (maxClosing,extraClosingBrackets)
            else:
                extraClosingBrackets -= 1
        return (maxClosing+1)//2

    def test(self):
        inputs = ["][][", "]]][[[", "[]", '']
        outputs = [1,2,0,0]
        for i in range(len(inputs)):
            print('test ' + str(i) + ': input=' + inputs[i] + ' output:' + str(self.minSwaps(inputs[i])) + ' expected is: ' + str(outputs[i]))      

s = Solution()
s.test()