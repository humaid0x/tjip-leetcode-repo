'''
TC: O(n * m)
  n is the number of strings in the input list
  m is the length of the longest string in the list

MC: O(1)
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = float("inf")
        baseStr = strs[0]
        for st in strs:
            currCommonPrefixLen = self.getCommonPrefixLen(st, baseStr)
            res = min(res, currCommonPrefixLen)
        return baseStr[:res]
    
    def getCommonPrefixLen(self, str1, str2):
        idx = 0
        minStrLen = min(len(str1), len(str2))
        while idx < minStrLen and str1[idx] == str2[idx]:
            idx += 1
        return idx

def testSolution():
    solution = Solution()
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["humaid"]) == "humaid"
    assert solution.longestCommonPrefix(["aaa", "bbb", "ccc"]) == ""
    assert solution.longestCommonPrefix([""]) == ""

testSolution()