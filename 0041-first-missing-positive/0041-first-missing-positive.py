class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 1
        for i in range(len(nums)):
            if res==nums[i]:
                res+=1
        return res
            