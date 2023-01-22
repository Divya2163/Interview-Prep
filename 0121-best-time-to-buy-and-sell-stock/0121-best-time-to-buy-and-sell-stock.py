class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        leftpt = 0 
        rightpt = 1
        while rightpt < len(prices):
            currprof = prices[rightpt]-prices[leftpt]
            if prices[leftpt]<prices[rightpt]:
                maxprof = max(currprof,maxprof)
            else:
                leftpt=rightpt
            rightpt+=1
        return maxprof
