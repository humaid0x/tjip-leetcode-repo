from collections import defaultdict
class Solution:
    def __init__(self):
        self.dupSubTrees = []
        self.hashes = defaultdict(int)

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dupSubTrees.clear()
        self.hashes.clear()
        self.generateHash(root)
        return self.dupSubTrees

    def generateHash(self, root):
        if root == None:
            return "#"

        left = self.generateHash(root.left)
        right = self.generateHash(root.right)
        curr = f"${root.val}, ${left}, ${right}"

        self.hashes[curr] += 1
        if self.hashes.get(curr) == 2:
            self.dupSubTrees.append(root)

        return curr
