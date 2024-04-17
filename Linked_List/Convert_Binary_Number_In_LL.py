'''
Problem (1290) Easy
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass
    def convert(self,head):
        cur = head
        val = 0
        while cur:
            val =  2*val+cur.val
            cur = cur.next
        return val
if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(0)

    # Creating an instance of the Solution class
    sol = Solution()

    # Converting the linked list to decimal
    result = sol.convert(head)

    # Printing the result
    print("Decimal value:", result)
