class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        i_min = nums.index(min(nums))
        i_max = nums.index(max(nums))
        
        a = min(i_min, i_max)
        b = max(i_min, i_max)
        
        # Strategy 1: Both from front (b + 1)
        # Strategy 2: Both from back (n - a)
        # Strategy 3: One from front, one from back (a + 1 + n - b)
        return min(b + 1, n - a, a + 1 + n - b)
