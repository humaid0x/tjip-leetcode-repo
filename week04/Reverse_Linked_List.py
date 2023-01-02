'''
TC: O(n) where n is the length of linked list
MC: O(n) for recursive function calls
'''

class Solution:
    def reverseList(self, currNode: Optional[ListNode]) -> Optional[ListNode]:
        if currNode == None or currNode.next == None:
            return currNode

        newHead = self.reverseList(currNode.next)
        currNode.next.next = currNode
        currNode.next = None

        return newHead
