'''
TC: O(n)
MC: O(1)
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maxLen = 0
        for uniqueChr in range(1, 27):
            currMaxLen = self.findMaxSubStrWithUniqueChr(s, k, uniqueChr)
            maxLen = max(maxLen, currMaxLen)
        return maxLen
    
    def findMaxSubStrWithUniqueChr(self, s, k, uniqueChr):
        L = R = maxLen = 0
        uniqueChrInBlock = 0
        cntCharAtLeastK = 0
        freq = [0 for _ in range(128)]

        while R < len(s):
            freq[ord(s[R])] += 1
            uniqueChrInBlock += freq[ord(s[R])] == 1
            cntCharAtLeastK += freq[ord(s[R])] == k
            R += 1

            while uniqueChrInBlock > uniqueChr:
                freq[ord(s[L])] -= 1
                uniqueChrInBlock -= freq[ord(s[L])] == 0
                cntCharAtLeastK -= freq[ord(s[L])] == k - 1
                L += 1
            
            if uniqueChrInBlock == cntCharAtLeastK:
                maxLen = max(maxLen, R - L)

        return maxLen

def testSolution():
    solution = Solution()
    assert solution.longestSubstring("aaabb", 3) == 3
    assert solution.longestSubstring("a", 3) == 0
    assert solution.longestSubstring("aaabb", 2) == 5 
    assert solution.longestSubstring("abcde", 1) == 5

testSolution()
