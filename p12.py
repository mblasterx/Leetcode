class Solution:
    def __init__(self):
        pass

    def fix_exceptions(self, input) -> str:
        '''
        Fixes the 6 exceptions in Roman numerals
        '''
        output = input
        exceptionDict = {'VIIII':'IX', 'IIII': 'IV', 'LXXXX':'XC', 'XXXX': 'XL', 'DCCCC':'CM', 'CCCC':'CD'}
        for key,value in exceptionDict.items():
            output = output.replace(key, value)
        return output

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

s = Solution()
print(s.intToRoman(1992))

# worked!