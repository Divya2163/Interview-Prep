class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            s=bin(i)
            s1=s[2:]
            lst.append(s1.count("1"))
        return lst 