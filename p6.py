class Solution:
    '''https://leetcode.com/problems/zigzag-conversion/
    '''
    def convert(self, s: str, numRows: int) -> str:
        '''
        '''
        if numRows == 1: # basecase
            return s

        outList = [ '' for _ in range(numRows)]
        vLength = 2*numRows-2 # size of a V zigzag shape
        for i in range((len(s) //vLength)+1):
            # test: print('s[' + str(vLength*i) + ':' + str(vLength*i+vLength) + ']=' + s[vLength*i:vLength*i+vLength])
            outList = [x+y for x,y in zip(outList,self.partial_convert(s[vLength*i:vLength*i+vLength], numRows))] # concatenate each V shape
        
        return ''.join(outList)

    def partial_convert(self, s:str, numRows:int) -> list:
        '''
        Does a V pattern and returns a list 
        '''
        outList = [ '' for _ in range(numRows) ] # initiate empty string list

        if len(s) <= numRows:   # if string has less chars than rows, it's easy
            for i in range(len(s)):
                outList[i] = s[i]
        else:
            for i in range(numRows):    # if string has more, first complete the rows
                outList[i] = s[i]
            for j in range(numRows, len(s)):
                outList[2*numRows-2-j] += s[j]  # then work on the diagonal bottom-left -> top-right, sum of indexes is always constant 2*numRows-2

        return outList

    def test(self) -> None:
        testCases = {
            ('PAYPALISHIRING',3)    :'PAHNAPLSIIGYIR',
            ('PAYPALISHIRING',4)    :'PINALSIGYAHRPI',
            ('A',1)                 :'A',
        }
        for (key,numRows),val in testCases.items():
            assert self.convert(key, numRows) == val
        print('All tests passed')
    
s = Solution()
s.test()
