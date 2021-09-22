class Solution:
    '''https://leetcode.com/problems/roman-to-integer/
    '''
    
    ROMAN_NUMS = {
        'I':1, 'V':5, 'X':10, 
        'L':50, 'C':100, 'D':500, 
        'M':1000,
    }
    SPECIAL_NUMS = {
        'IV': 4, 'IX': 9, 'XL':40, 
        'XC': 90, 'CD': 400, 'CM': 900,
    }

    def romanToInt(self, s: str) -> int:
        '''First solution
        '''
        # cases for IV, IX, XL, XC, CD, CM
        for key,val in self.SPECIAL_NUMS.items():
            while key in s: 
                s = s.replace(key,'+' + str(val)) # everything is additive 
        for key,val in self.ROMAN_NUMS.items():
            while key in s:
                s = s.replace(key, '+' + str(val))
        # we use the eval function
        return eval(s)
        # we possibly have an extra + at the beginning of the string so we cut it out, then we make it into a list
        # return sum(int(x) for x in s.strip('+').split('+'))

    def romanToInt(self, s: str) -> int:
        '''Second solution: fast using map
        '''
        romanNums = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000,
            
            'a':4, 
            'b':9, 
            'c':40, 
            'd':90, 
            'e':400, 
            'f':900,
        }
        # translate to fit our dictionary
        s = s.replace('IV', 'a').replace('IX', 'b').replace('XL', 'c').replace('XC', 'd').replace('CD', 'e').replace('CM', 'f')

        return sum(map(romanNums.get, s))

    def test(self) -> None:
        testCases = {
            'III'       :3, 
            'IV'        :4,
            'IX'        :9, 
            "LVIII"     :58, 
            "MCMXCIV"   :1994,
        }
        for key,val in testCases.items():
            assert self.romanToInt(key) == val 
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()