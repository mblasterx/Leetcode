# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''Given a string s, returns the longest palindromic substring in s.
        '''
        maxSlice = ''

        for i in range(len(s)): # odd length palindromes can start at any character and expand to the left and right
            currentMaxSlice = self.find_max_palindromic_slice(s, left = i, right = i)
            if len(maxSlice) < len(currentMaxSlice):
                maxSlice = currentMaxSlice

        for i in range(0, len(s)): # even length palindromes 
            currentMaxSlice = self.find_max_palindromic_slice(s, left = i, right = i+1)
            if len(maxSlice) < len(currentMaxSlice):
                maxSlice = currentMaxSlice 

        return maxSlice

    def find_max_palindromic_slice(self, s: str, left: int, right: int) -> str:
        '''Find the max palindromic slice extending outwards from s[left:right+1] 
        '''
        currentSlice = ''
        j = 0
        while left-j>=0 and right+j<len(s):   # make sure we don't go outside the slice when we reach either left or right endpoints
            if s[left-j] == s[right+j]: # if the endpoints are equal, they're part of the palindromic slice
                if currentSlice == '': 
                    currentSlice = s[left-j:right+j+1]
                else:
                    currentSlice = s[left-j] + currentSlice + s[right+j]
            else:   # if the endpoints are different we're done with the loop
                break
            j+=1

        return currentSlice

s = Solution()
testList = ['a', 'aa', 'aaa', 'abab', 'ababa', 'xaabaya', '987111', 'aabbxa']
testStr = testList[-1]
print(s.longestPalindrome(testStr))