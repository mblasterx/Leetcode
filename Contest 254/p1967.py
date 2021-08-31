'''
Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
'''

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for pat in patterns:
            if pat in word:
                count += 1

        return count

s = Solution()
patterns = ["a","b","c"]
word = 'aaaaabbbbb'
print(s.numOfStrings(patterns, word))