'''
TC: O(n) where n is the number of nodes in the tree
MC: O(log(n))
'''

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None or root.left == None:
            return root

        root.left.next = root.right
        root.right.next = root.next and root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root