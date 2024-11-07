class Node:
    def __init__(self,data=None,next=None,prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
def traverse(head):
    current = head
    while