class Solution:
    '''https://leetcode.com/problems/regular-expression-matching/
    '''
    def isMatch_recursive(self, s: str, p: str) -> bool:
        '''
        Returns true if the expression matches and false if not
        * = 0 or more of the previous character
        . = any 1 character
        '''

        if not p:   # empty string 
            return not s

        first_match = s != '' and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        return False

    def isMatch(self, text, pattern):
        '''
        '''
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)] # initialize the dynamic programming array

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]

    def test(self) -> None:
        testCases = {
            ("abcccea", 'abd*c.*e.')    :True,      # we got a pattern match
            ('abcd', 'ab.e')            :False,     # no match
            ('asd2321asdsaevas', '.*')  :True,      # .* should match everything
        }
        for (text, pattern),val in testCases.items():
            assert self.isMatch(text, pattern) == val
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()