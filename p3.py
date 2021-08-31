class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''https://leetcode.com/problems/longest-substring-without-repeating-characters/
        '''

        maxLength = 0 # init result variable
        for i in range(len(s)):
            j = 1
            curMaxLength = 1    # s[i] is the first distinct character in substring
            while i+j < len(s):     # keep going through the substring until we get a double, or we reach the end of the string
                if s[i+j] in s[i:i+j]:
                    break
                else:
                    curMaxLength += 1
                    j+=1
            maxLength = max(maxLength,curMaxLength) # update the max if needed
            if len(s)-i < maxLength:  # we can make it slightly faster by not going all the way to the end of the string
                break

        return maxLength

    def test(self):
        testCases = {'aab':2, 'abcabcbb':3, 'bbbbb':1, 'pwwkew':3, '':0}
        for key,val in testCases.items():
            print('Test str: ' + key + ' returns ' + str(self.lengthOfLongestSubstring(key)) + ' and should return ' + str(val))


s = Solution()
s.test()