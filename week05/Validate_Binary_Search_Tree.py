'''
TC: O(n) where n is the total number of nodes
MC: O(h) where h is the height of tree.
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, node, minimum, maximum):
        if not node:
            return True
        if node.val < minimum or node.val > maximum:
            return False
        
        left = self.helper(node.left, minimum, node.val - 1)
        right = self.helper(node.right, node.val + 1, maximum)
        
        return left&right
