'''
TC: O(n) where n is the total number of nodes
MC: O(h) where h is the height of tree.
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:return
        if root.val == p.val or root.val == q.val:return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right
        