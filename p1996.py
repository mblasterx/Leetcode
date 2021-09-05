from typing import List
class Solution:
    '''https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
    '''
    def numberOfWeakCharacters_v1(self, properties: List[List[int]]) -> int:
        '''Brute force, first attempt
        '''
        def is_weak(char1: List[int], char2: List[int]) -> int:
            '''Returns 1 if char1 is weak vs char2, None otherwise
            '''
            if (char1[1] < char2[1] and char1[0] < char2[0]):
                return 1

        properties.sort()
        numWeak = 0
        for i in range(len(properties)):
            for j in range(len(properties)):
                if i == j:
                    continue
                if properties[i] == properties[j]:
                    continue
                if is_weak(properties[i],properties[j]):
                    numWeak += 1
                    break
        return numWeak

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        '''More efficient attempt
        '''
        properties.sort(key=lambda x:(-x[0], x[1])) # decreasing by the attack, increasing by the defense with attack is the same
        # this means an player cannot be weaker than any players to its right, so we only look to the left to see if current player is weak as we parse the sorted list
        numWeak = 0
        maxCurrent = 0
        for attack, defense in properties: 
            if defense < maxCurrent:
                numWeak += 1
            else:
                maxCurrent = defense    # the first player after sorting is never weak as it has max attack
        return numWeak

    def test(self) -> None:
        ''' Constraints
        2 <= properties.length <= 105
        properties[i].length == 2
        1 <= attacki, defensei <= 105
        '''
        testCases = [   # tuples of any variables we need to test
            ([[5,5],[6,3],[3,6]],       0),
            ([[2,2],[3,3]],             1),
            ([[1,5],[10,4],[4,3]],      1),
            ([[2,2],[2,2]],             0),
            ([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]],   6),
        ]
        
        for (properties, expectedResult) in testCases:
            assert self.numberOfWeakCharacters(properties) == expectedResult, (properties, expectedResult, self.numberOfWeakCharacters(properties))
        print('All tests passed')
    
s = Solution()
s.test()