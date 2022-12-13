 class Solution:
    # TC: O(m + n)
    # MC: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1

        while idx1 != -1 and idx2 != -1:
            if nums1[idx1] < nums2[idx2]:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            idx -= 1
        
        while idx1 != -1:
            nums1[idx] = nums1[idx1]
            idx1 -= 1
            idx -= 1

        while idx2 != -1:
            nums1[idx] = nums2[idx2]
            idx2 -= 1
            idx -= 1        
