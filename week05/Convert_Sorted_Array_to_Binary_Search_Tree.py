'''
TC: O(nlogn) where n is the size of the nums array
MC: O(n)
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums) - 1)

    def makeBST(self, nums, start, end):
        if end < start:return None

        mid = (start + end) // 2
        left = self.makeBST(nums, start, mid - 1)
        right = self.makeBST(nums, mid + 1, end)

        return TreeNode(nums[mid], left, right)
