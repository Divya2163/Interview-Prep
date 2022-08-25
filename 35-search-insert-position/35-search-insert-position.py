class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
            else:
                nums.insert(0,target)
                nums=sorted(nums)
                return nums.index(target)