class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for i in range(n+1):
            lst.append(bin(i).count("1"))
        return lst 