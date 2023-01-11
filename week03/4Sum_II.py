from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pairSum = defaultdict(int)

        for x in nums1:
            for y in nums2:
                pairSum[x + y] += 1
        
        tupleCnt = 0
        for x in nums3:
            for y in nums4:
                if pairSum.get(-(x + y)):
                    tupleCnt += pairSum[-(x + y)]
        
        return tupleCnt