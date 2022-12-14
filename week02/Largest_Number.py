'''
TC: O(nlogn)
MC: O(n)
'''

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
      
        def compare(n, m):
            if n + m < m + n:
                return 1
            return -1

        arr = list(map(str, nums))
        arr.sort(key=cmp_to_key(compare))
        res = "".join(arr)

        if int(res) == 0:
            return "0"
        return res

def testSolution():
    solution = Solution()
    assert solution.largestNumber([10, 2]) == "210"
    assert solution.largestNumber([0, 0]) == "0"
    assert solution.largestNumber([10]) == "10"

testSolution()