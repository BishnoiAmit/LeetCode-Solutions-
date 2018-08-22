"""
PROBLEM: 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their
nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example: 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
Created on Wed Aug 22 16:46:49 2018

@author: bishnoiamit
"""

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = []
        carry = 0
        
        while(l1 or l2):
            if (l1 and l2):
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif(l1 and not l2):
                sum = l1.val + carry
                l1 = l1.next
            else:
                sum = l2.val + carry
                l2 = l2.next
            
            if sum > 9:
                carry = int(sum / 10)
                l3.append(sum%10)
                print(l3)
                
            else:
                carry = 0
                l3.append(sum)
        
        if(carry == 1 and not l1 and not l2):
            l3.append(1)
        
        if(l1 != 'null'):
            while(l1):
                l3.append((l1.val)+carry)
                l1 = l1.next
        
        if(l2 != 'null'):
            while(l2):
                l3.append((l2.val)+carry)
                l2 = l2.next
                
        return l3

def main():
    obj = Solution()
    l1 = [2,4,3]
    l2 = [5,6,4]
    print(obj.addTwoNumbers(l1,l2))
    
main()
