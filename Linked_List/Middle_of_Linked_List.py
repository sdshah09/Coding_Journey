'''
Problem 876 (Easy)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass
    def getlength(self,head):
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        return length
    def middle(self,head):
        length = self.getlength(head)
        cur = head
        pos = 0
        while cur:
            if pos==length//2:
                return cur
            pos+=1
            cur = cur.next


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Creating an instance of the Solution class
    sol = Solution()

    # Converting the linked list to decimal
    result = sol.middle(head)

    # Printing the result
    print("Decimal value:", result.val)
