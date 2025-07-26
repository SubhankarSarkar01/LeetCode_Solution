# -- 3381. Maximum Subarray Sum With Length Divisible by K --
from typing import List
from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum_remainders = [inf] * k
        
        max_sum = -inf
        
        current_sum = prefix_sum_remainders[-1] = 0

        for i, num in enumerate(nums):
            
            current_sum += num
            
            max_sum = max(max_sum, current_sum - prefix_sum_remainders[i % k])
            
            prefix_sum_remainders[i % k] = min(prefix_sum_remainders[i % k], current_sum)

        return max_sum
        