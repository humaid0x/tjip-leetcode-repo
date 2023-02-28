'''
TC: O(n) where n is the total number of nodes
MC: O(h) where h is the height of tree.
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path_sm = root.val
        self.dfs(root)
        return self.path_sm

    def dfs(self, node):
        if node == None:return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.path_sm = max(self.path_sm, left + right + node.val)
       
        return max(0, max(left, right) + node.val)