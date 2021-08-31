# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''Given a string s, returns the longest palindromic substring in s.
        '''
        maxSlice = s[0]
        # only works for even palindromes
        for i in range(len(s)-1):
            j = 0 # temp var that keeps track how many equal endspoints there are after a double character is founds
            if s[i] == s[i+1]:
                slice = s[i:i+2] # keeps track of the actual palindrome
                while j<i and i+1+j<len(s)-1:
                    if s[i-j] != s[i+1+j]:
                        break
                    else:
                        slice = s[i-j] + slice + s[i-j]
                    j +=1 
            if len(maxSlice) < 2*j:
                maxSlice = slice
        
        # odd palindromes 
        for i in range(1,len(s)-1):
            j = 0 # temp var 
            if s[i-1] == s[i+1]:
                slice = s[i-1:i+2] # keeps track of the current palindrome letters 
                while j<i-1 and i+1+j<len(s)-1:
                    if s[i-1-j] != s[i+1+j]:
                        break
                    else:
                        slice = s[i-1-j] + slice + s[i-1-j] # update slice with new equal endpoints
                    j +=1 

                if len(maxSlice) < 2*j+1:
                    maxSlice = slice

        return maxSlice

# not passing certain tests 

s = Solution()
testStr = 'ababa'
print(s.longestPalindrome(testStr))