def signFunc(x):
    if x==0:
        return 0
    elif x>0:
        return 1
    else:
        return -1
    
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product = product*i
        return signFunc(product)