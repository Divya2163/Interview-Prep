class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        res=""
        n=len(s)
        def nice(start,end):
                t=set(s[start:end])
                for i in t:
                    if (i.lower() in t) != (i.upper() in t):
                        return False
                return True 
        
        for start in range(n):
            for end in range(start+1,n+1):
                if nice(start,end) and end - start >len(res):
                    res=s[start:end]
        return res