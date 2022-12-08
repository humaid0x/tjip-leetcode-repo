 class Solution:
    # TC: O(n)
    # MC: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        xr = 0
        for num in nums:
            xr ^= num
        return xr
