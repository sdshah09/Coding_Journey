'''

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self) -> None:
        pass
    def reverse(self,head):
        if head is None:
            return None
        if head.next is None:
            return head

        cur = head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    
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
    reversed_head = sol.reverse(head)

    # Printing the result
    while reversed_head:
        print(reversed_head.val, end=" -> ")
        reversed_head = reversed_head.next
