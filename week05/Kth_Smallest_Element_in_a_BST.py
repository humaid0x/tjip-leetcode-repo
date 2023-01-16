'''
TC: O(n) where n is the total number of nodes
MC: O(h) where h is the height of tree.
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if node == None:return
        self.helper(node.left)
        
        self.cnt -= 1
        if self.cnt == 0:
            self.res = node.val

        self.helper(node.right)

