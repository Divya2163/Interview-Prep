class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            t = set(s[i:i+3])
            if len(t)==3:
                count+=1
        return count
            