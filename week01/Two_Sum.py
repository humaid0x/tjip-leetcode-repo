 class Solution:
    # TC: O(n)
    # MC: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNumToIdx = {}
        for idx, num in enumerate(nums):
            mapNumToIdx[num] = idx
            
        for idx, num in enumerate(nums):
            requiredNum = target - num
            if requiredNum not in mapNumToIdx:
                continue
            if mapNumToIdx[requiredNum] == idx:
                continue
            return [idx, mapNumToIdx[requiredNum]]
