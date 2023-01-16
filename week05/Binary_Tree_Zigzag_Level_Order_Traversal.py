'''
TC: O(n) where n is the total number of nodes
MC: O(n)
'''

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        level = 0
        
        while q:
            curr = deque()
            currLvlSize = len(q)
            for _ in range(currLvlSize):
                node = q.popleft()

                if level % 2 == 0:curr.append(node.val)
                else:curr.appendleft(node.val)
                    
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)

            res.append(curr)
            level += 1

        return res 
        