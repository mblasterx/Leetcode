from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        returnStr = 'ListNode: ' + str(self.val)
        while self.next:
            self = ListNode(self.next)
            returnStr += '->' + str(self.val)
        return returnStr

class Solution:
    '''https://leetcode.com/problems/merge-two-sorted-lists/
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = ListNode()
        right = left
        
        while l1 and l2:
            if l1.val < l2.val:
                right.next = l1
                l1 = l1.next
            else:
                right.next = l2
                l2 = l2.next
            # update the right pointer
            right = right.next

        if l1:
            right.next = l1
        elif l2:
            right.next = l2

        return left.next

    def test(self) -> None:

        testCases = [   # tuples of any variables we need to test
        ]
        
        for (l1, l2, expectedResult) in testCases:
            print(l1)
            assert self.mergeTwoLists(l1,l2) == expectedResult, (l1, l2, expectedResult, self.mergeTwoLists(l1,l2))
        print('All tests passed')
    
def main():
    s = Solution()
    s.test()

if __name__ == '__main__':
    main()