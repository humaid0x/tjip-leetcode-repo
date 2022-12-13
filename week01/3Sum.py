 class Solution:
    # TC: O(n^2)
    # MC: O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums) - 2):
            startIdx = i + 1
            endIdx = len(nums) - 1
            while startIdx < endIdx:
                currSum = nums[i] + nums[startIdx] + nums[endIdx]
                if currSum < 0:
                    startIdx += 1
                elif currSum > 0:
                    endIdx -= 1
                else:
                    triplets.add((nums[i], nums[startIdx], nums[endIdx]))
                    startIdx += 1
                    endIdx -= 1

        return [list(triplet) for triplet in triplets]
