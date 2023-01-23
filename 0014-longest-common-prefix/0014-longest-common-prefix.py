class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i, c in enumerate(a):
            for s in strs:
                if len(s) == i or s[i] != c:
                    return a[:i]
        return a
