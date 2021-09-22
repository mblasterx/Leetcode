from typing import List
class Solution:
    '''https://leetcode.com/problems/longest-common-prefix/
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''There is at least 1 string in strs
        '''
        shortestWord = min(strs, key=len)       # find the shortest word, it will be the max prefix
        for i in range(len(shortestWord)):      # go letter by letter
            for word in strs:                   # every time we find a word in our list that doesn't have all the prefix we end it there
                if word[i] != shortestWord[i]:
                    return shortestWord[:i]
        # care for when 1 word, or all words are the same
        return shortestWord


    def test(self) -> None:
        testCases = {
            0       :'fl',
            1       :'',
            2       :'prefix',
            3       :'',
        }
        testList = [
            ["flower","flow","flight"],
            ["dog","racecar","car"],
            ["prefix"],
            ["", "b"],
        ]
        for key,val in testCases.items():
            assert self.longestCommonPrefix(testList[key]) == val, testList[key]
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()