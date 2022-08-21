class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[str(i) for i in digits]
        n=int("".join(s))
        res=n+1
        num=list(map(int,str(res)))
        return num
        