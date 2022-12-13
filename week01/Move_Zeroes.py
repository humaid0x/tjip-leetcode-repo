class Solution:
    # TC: O(n)
    # MC: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx = -1
        for idx, num in enumerate(nums):
            if zeroIdx == -1 and num == 0:
                zeroIdx = idx
            if zeroIdx == -1:
                continue
            if num != 0:
                nums[zeroIdx] = num
                zeroIdx += 1
                
        if zeroIdx == -1:
            return
        while zeroIdx < len(nums):
            nums[zeroIdx] = 0
            zeroIdx += 1       
