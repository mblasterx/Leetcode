class Solution:
    '''https://leetcode.com/problems/integer-to-roman/
    '''
    def intToRoman(self, num: int) -> str:
        '''
        Returns a roman numeral from integer
        '''
        romanDict = {1000:'M', 500:'D', 100:'C', 50:'L',  10:'X', 5:'V', 1:'I'}
        output = ''
        for key,value in romanDict.items():
            if num//key > 0:
                output += value*(num//key)
                num -= (num//key) * key
        
        return self.fix_exceptions(output)

    def fix_exceptions(self, input) -> str:
        '''
        Fixes the 6 exceptions in Roman numerals
        '''
        output = input
        exceptionDict = {'VIIII':'IX', 'IIII': 'IV', 'LXXXX':'XC', 'XXXX': 'XL', 'DCCCC':'CM', 'CCCC':'CD'}
        for key,value in exceptionDict.items():
            output = output.replace(key, value)
        return output

    def test(self) -> None:
        testCases = {
            3       :'III',
            4       :'IV',
            9       :'IX',
            58      :'LVIII',
            48      :'XLVIII',
            1994    :'MCMXCIV',
        }
        for key,val in testCases.items():
            assert self.intToRoman(key) == val 
        print('All tests passed')
    
s = Solution()
s.test()