# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = []
        carry = 0
        n1, n2 = len(l1), len(l2)
        for i in range(max(n1,n2)):
            sumOfDigits = carry
            if i < n1:
                sumOfDigits += l1[i]
            if i < n2:
                sumOfDigits += l2[i]
            if sumOfDigits < 10:
                sum.append(sumOfDigits)
                carry = 0
            else:
                sum.append(sumOfDigits%10)
                carry = 1
        if carry == 1: # append last 1 
            sum.append(1)
            
        return sum
        

a = [9,9,9,9,9,9,9] 
b = [9,9,9,9]

s = Solution()

print(s.addTwoNumbers(a,b))