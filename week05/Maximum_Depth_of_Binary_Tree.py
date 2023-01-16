'''
TC: O(n) where n is the total number of nodes
MC: O(h) where h is the height of tree.
'''

class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node == None:return 0

        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)

        return 1 + max(left, right)