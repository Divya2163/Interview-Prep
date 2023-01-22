class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = sorted(nums, reverse=True)
        return res[k-1]