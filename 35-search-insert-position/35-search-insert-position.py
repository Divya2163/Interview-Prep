class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)+1):
            mini=i
            if target==nums[i]:
                return i
            else:
                nums.insert(0,target)
                nums=sorted(nums)
                return nums.index(target)