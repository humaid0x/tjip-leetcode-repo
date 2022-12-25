'''
TC: O(n)
MC: O(1)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = [0 for _ in range(128)]
        L = R = repeatCnt = maxSubStrLen = 0

        while R < len(s):
            freq[ord(s[R])] += 1
            if freq[ord(s[R])] > 1:
              repeatCnt += 1

            while repeatCnt > 0:
                freq[ord(s[L])] -= 1
                if freq[ord(s[L])] == 1:
                    repeatCnt -= 1
                L += 1

            maxSubStrLen = max(maxSubStrLen, R - L + 1)
            R += 1

        return maxSubStrLen

def testSolution():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3 
    assert solution.lengthOfLongestSubstring("aaa") == 1 
    assert solution.lengthOfLongestSubstring("") == 0 

testSolution()