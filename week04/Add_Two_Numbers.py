'''
TC: O(max(n, m))
    n: length of l1
    m: length of l2
    
MC: O(max(n, m))
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        sm = 0

        while l1 or l2 or sm:
            if l1:
                sm += l1.val
                l1 = l1.next
            
            if l2:
                sm += l2.val
                l2 = l2.next
            
            dummy.next = ListNode(sm % 10)
            dummy = dummy.next

            sm //= 10
     
        return head.next
