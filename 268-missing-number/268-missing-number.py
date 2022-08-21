class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0,len(nums)+1):
            if i >= len(nums):
                return i
            elif i != nums[i]:
                return i
        