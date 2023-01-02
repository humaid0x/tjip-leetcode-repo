'''
TC: O(n) where n is the length of linked list
MC: O(1)
'''

class Solution:
    def reverseList(self, currNode):
        if currNode == None or currNode.next == None:
            return currNode

        newHead = self.reverseList(currNode.next)
        currNode.next.next = currNode
        currNode.next = None

        return newHead


    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        revHead = self.reverseList(slow)
        revHeadCopy = revHead

        maxTwinSum = 0
        while revHead:
            currTwinSum = head.val + revHead.val
            maxTwinSum = max(maxTwinSum, currTwinSum)
            head = head.next
            revHead = revHead.next
        
        self.reverseList(revHeadCopy)

        return maxTwinSum

