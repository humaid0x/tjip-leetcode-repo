'''
TC: O(n)
MC: O(1)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False

        freq = [0 for _ in range(26)]
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for n in freq:
            if n != 0:return False

        return True 

def testSolution():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram") == True
    assert solution.isAnagram("abc", "b") == False
    assert solution.isAnagram("aaaa", "a") == False

testSolution()