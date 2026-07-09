from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        """
        Determines if paths exist between pairs of indices based on a maximum difference constraint.

        Args:
            n: The number of elements
            nums: Array of values at each position
            maxDiff: Maximum allowed difference between consecutive elements
            queries: List of [u, v] pairs to check path existence

        Returns:
            List of boolean values indicating if path exists for each query
        """
        # Initialize group/component array for each position
        # This tracks which connected component each index belongs to
        group_id = [0] * n

        # Counter for number of "breaks" in the path
        # A break occurs when consecutive elements differ by more than maxDiff
        current_group = 0

        # Iterate through consecutive pairs to identify breaks
        for i in range(1, n):
            # Check if difference between consecutive elements exceeds maxDiff
            if nums[i] - nums[i - 1] > maxDiff:
                # Increment group counter when a break is found
                current_group += 1

            # Assign current group ID to this position
            group_id[i] = current_group

        # For each query [u, v], check if both indices are in the same group
        # If they share the same group ID, a valid path exists between them
        result = [group_id[u] == group_id[v] for u, v in queries]

        return result
