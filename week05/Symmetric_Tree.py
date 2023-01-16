'''
TC: O(n) where n is the total number of nodes
MC: O(n)
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isTwoNodeSymmentric(root.left, root.right)

    def isTwoNodeSymmentric(self, left, right):
        if left == None or right == None:
            return True if left == right else False

        if left.val != right.val:
            return False
        
        checkLeft = self.isTwoNodeSymmentric(left.left, right.right)
        checkRight = self.isTwoNodeSymmentric(left.right, right.left)

        return checkLeft and checkRight
