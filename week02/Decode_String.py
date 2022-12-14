'''
TC: O(n)
MC: O(n)
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currStr = ""
        k = 0

        for c in s:
            if c.isdigit():
                k *= 10
                k += int(c)
            elif c == "[":
                stack.append([currStr, k])
                currStr = ""
                k = 0
            elif c == "]":
                lastStr, lastK = stack.pop()
                currStr = lastStr + lastK * currStr
            else:
                currStr += c

        return currStr

def testSolution():
    solution = Solution()
    assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
    assert solution.decodeString("3[a2[b1[c]]]") == "abcbcabcbcabcbc"

testSolution()
