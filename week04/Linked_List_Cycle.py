'''
TC: O(n) where n is the length of linked list
MC: O(1)
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:return True
        return False
