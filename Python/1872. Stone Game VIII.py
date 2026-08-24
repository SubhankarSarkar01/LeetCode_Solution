from typing import List
from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate prefix sums for quick range sum calculation
        # prefix_sums[i] represents sum of stones[0] to stones[i]
        prefix_sums = list(accumulate(stones))
      
        @cache
        def calculate_max_score_difference(current_index: int) -> int:
            """
            Calculate the maximum score difference the current player can achieve
            starting from current_index.
          
            Args:
                current_index: The index from which the current player can choose
          
            Returns:
                Maximum score difference (current player score - opponent score)
            """
            # Base case: if we're at or past the second-to-last stone,
            # the only option is to take all remaining stones
            if current_index >= len(stones) - 1:
                return prefix_sums[-1]
          
            # The current player has two choices:
            # Option 1: Skip this position and let the decision move to next index
            skip_current = calculate_max_score_difference(current_index + 1)
          
            # Option 2: Take stones from 0 to current_index (score = prefix_sums[current_index])
            # Then the opponent plays optimally from current_index + 1
            # Score difference = our score - opponent's best score
            take_current = prefix_sums[current_index] - calculate_max_score_difference(current_index + 1)
          
            # Return the maximum score difference we can achieve
            return max(skip_current, take_current)
      
        # Start from index 1 (at least 2 stones must be taken initially)
        return calculate_max_score_difference(1)
