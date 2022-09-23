class Solution:
    def concatenatedBinary(self, n: int) -> int:
        lst=[]
        for i in range(0,n+1):
            i=bin(i)
            lst.append(i[2:])
        sq=''.join(lst)
        result = int(sq,2)
        return result % (10**9 + 7)
        