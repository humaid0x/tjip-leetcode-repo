class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.len = 0
        self.head = Node()


    def get(self, index: int) -> int:
        if index < 0 or self.len <= index:
            return -1

        curr = self.head.next
        while index:
            curr = curr.next
            index -= 1

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len, val)

        
    # TC: O(n) where n is the length of linked list
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or self.len < index:return

        curr = self.head
        while index:
            curr = curr.next
            index -= 1

        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.len += 1
        

    # TC: O(n) where n is the length of linked list
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.len <= index:return

        curr = self.head
        while index:
            curr = curr.next
            index -= 1

        curr.next = curr.next.next
        self.len -= 1
        