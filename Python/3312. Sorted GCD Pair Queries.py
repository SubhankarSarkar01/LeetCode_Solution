from typing import List
from collections import Counter
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Find the maximum value in nums to determine the range
        max_value = max(nums)

        # Count frequency of each number in nums
        frequency_count = Counter(nums)

        # Array to store count of pairs with GCD equal to index
        gcd_pair_count = [0] * (max_value + 1)

        # Calculate GCD counts from largest to smallest using inclusion-exclusion principle
        for gcd in range(max_value, 0, -1):
            # Count numbers that are multiples of current gcd
            multiples_count = 0

            # Iterate through all multiples of current gcd
            for multiple in range(gcd, max_value + 1, gcd):
                multiples_count += frequency_count[multiple]
                # Subtract pairs already counted with larger GCDs (inclusion-exclusion)
                gcd_pair_count[gcd] -= gcd_pair_count[multiple]

            # Add number of pairs that can be formed from multiples
            # Using combination formula: C(n, 2) = n * (n - 1) / 2
            gcd_pair_count[gcd] += multiples_count * (multiples_count - 1) // 2

        # Create prefix sum array for binary search
        prefix_sum = list(accumulate(gcd_pair_count))

        # For each query, find the GCD value using binary search on prefix sum
        return [bisect_right(prefix_sum, query) for query in queries]
