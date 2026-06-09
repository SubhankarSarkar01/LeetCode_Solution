class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        cal = max(nums) - min(nums)
        return cal*k
        
