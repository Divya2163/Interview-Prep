class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumb = nums[0]
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum=0
            cursum += n
            sumb = max(sumb,cursum)
        return sumb
