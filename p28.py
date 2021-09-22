class Solution:
    '''https://leetcode.com/problems/implement-strstr/
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        '''The str.find() method does this exact thing
        '''
        return haystack.find(needle)
        
    def test(self) -> None:
        testCases = {
            ('hello', 'll')     :2,
            ('aaaaa', 'bba')    :-1,
            ('', '')            :0,
            ('aaaa', '')        :0,
        }
        for (haystack, needle),val in testCases.items():
            assert self.strStr(haystack, needle) == val, (haystack, needle, val)
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()