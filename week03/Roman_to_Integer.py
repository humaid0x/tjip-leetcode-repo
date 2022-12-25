'''
TC: O(n)
	n is the size of string s

MC: O(1) 
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        symToVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = prevVal = 0
        for sym in s[::-1]:
            currVal = symToVal[sym]
            res += currVal if currVal >= prevVal else -1 * currVal
            prevVal = currVal

        return res
