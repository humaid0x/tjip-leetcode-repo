'''
TC: O(n)
MC: O(n)
'''

from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            strHash = self.getHash(s)
            groups[strHash].append(s)
        return groups.values()

    def getHash(self, s):
        BASE = 997
        MOD = 101103107109113
        H = 1
        for c in s:
            H *= BASE + ord(c)
            if H >= MOD: H %= MOD
        return H