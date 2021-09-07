from typing import List
class Solution:
    '''https://leetcode.com/problems/longest-common-subsequence/
    '''

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
        '''
        # Recursive + memoization built in
        # dp[i][j] = self.longestCommonSubsequence(text1[:i], text2[:j])
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:    # if the two letters are equal at i, j then we add 1 to the possible result, and look at i+1, j+1
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])  # if they aren't equal the longest substring can start at j+1 and include i or at i+1 and include j 

        return dp[len(text1)][len(text2)]

    def test(self) -> None:
        testCases = [   # tuples of any variables we need to test
            ("abcde",       "ace",          3),
            ("abc",         "abc",          3),
            ("abc",         "def",          0),
            ("shinchan",    "noharaaa",     3), # "nha"
            ("fmymaw",  "awyfm",   2), # "fm"
            ("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq", 6),
        ]
        
        for (text1, text2, expectedResult) in testCases:
            assert self.longestCommonSubsequence(text1,text2) == expectedResult , (text1, text2, expectedResult, self.longestCommonSubsequence(text1,text2))
        print('All tests passed')
    
s = Solution()
s.test()