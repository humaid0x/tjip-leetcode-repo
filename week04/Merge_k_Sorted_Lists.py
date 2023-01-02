'''
TC: O(n * log(k))
    k: number of linked lists
    n: total number of nodes in all the linked lists
    
MC: O(n * log(k))
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.helper(0, len(lists) - 1, lists)

    def helper(self, L, R, lists):
        if L > R:return
        if L == R:return lists[L]

        M = (L + R) // 2
        left = self.helper(L, M, lists)
        right = self.helper(M + 1, R, lists)
        return self.mergeTwoLists(left, right)


    def mergeTwoLists(self, left, right):
        dummy = ListNode()
        head = dummy

        while left and right:
            vleft = left.val
            vright = right.val
            if vleft < vright:
                dummy.next = ListNode(vleft)
                left = left.next
            else:
                dummy.next = ListNode(vright)
                right = right.next
            dummy = dummy.next
           
        while left:
            dummy.next = ListNode(left.val)
            dummy = dummy.next
            left = left.next

        while right:
            dummy.next = ListNode(right.val)
            dummy = dummy.next
            right = right.next

        return head.next
