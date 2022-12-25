'''
TC: O(s + n * m * logm) 
    s is the length of the string
    n is the number of words
    m is the length of the longest string in the list
    
MC: O(s)
'''

from bisect import bisect_left
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        chrIdxArr = [[] for _ in range(26)]
        for idx, char in enumerate(s):
            chrIdxArr[ord(char) - ord('a')].append(idx)

        res = 0
        for word in words:
            res += self.isSubsequence(word, chrIdxArr)
        return res

    def isSubsequence(self, word, chrIdxArr):
        prevIdx = -1
        for idx, char in enumerate(word):
            currChrIdxArr = chrIdxArr[ord(char) - ord('a')]
            nxt = bisect_left(currChrIdxArr, prevIdx + 1)
            if nxt == len(currChrIdxArr):
                return False
            prevIdx = currChrIdxArr[nxt]
        return True

def testSolution():
    solution = Solution()
    assert solution.numMatchingSubseq("abcde", ["a","bb","acd","ace"]) == 3
    assert solution.numMatchingSubseq("edcba", ["a","bb","acd","ace"]) == 1
   
testSolution()
