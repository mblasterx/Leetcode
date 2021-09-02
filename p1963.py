class Solution:
    '''https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
    '''
    def minSwaps(self, s: str) -> int:
        '''
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
        inputs = []
        outputs = [1,2,0,0]
        for i in range(len(inputs)):
            print('test ' + str(i) + ': input=' + inputs[i] + ' output:' + str(self.minSwaps(inputs[i])) + ' expected is: ' + str(outputs[i]))      

    def test(self) -> None:
        testCases = {
            "][]["      :1,
            "]]][[["    :2,
            "[]"        :0,
            ''          :0,
        }
        for key,val in testCases.items():
            assert self.minSwaps(key) == val 
        print('All tests passed')

s = Solution()
s.test()