'''
TC: O(n)
MC: O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:return False

        stack = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for p in s:
            if p in "({[":
                stack.append(p)
            elif stack and parentheses[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack

def testSolution():
    solution = Solution()
    assert solution.isValid("()()()") == True
    assert solution.isValid("(()){[]}") == True
    assert solution.isValid("()(") == False
    assert solution.isValid("))") == False
    assert solution.isValid("()))") == False

testSolution()