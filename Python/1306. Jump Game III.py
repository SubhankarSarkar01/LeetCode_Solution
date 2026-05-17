#-- 1306. Jump Game III --
from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Determine if we can reach any index with value 0 in the array.
        From index i, we can jump to i + arr[i] or i - arr[i].
      
        Args:
            arr: List of non-negative integers representing jump distances
            start: Starting index position
          
        Returns:
            True if we can reach an index with value 0, False otherwise
        """
        # Initialize BFS queue with starting position
        queue = deque([start])
      
        # BFS traversal to find if we can reach value 0
        while queue:
            # Get current index from queue
            current_index = queue.popleft()
          
            # Check if we've reached target (value is 0)
            if arr[current_index] == 0:
                return True
          
            # Store jump distance before marking as visited
            jump_distance = arr[current_index]
          
            # Mark current index as visited by setting to -1
            arr[current_index] = -1
          
            # Try both possible jumps: forward and backward
            for next_index in (current_index + jump_distance, current_index - jump_distance):
                # Check if next index is valid and unvisited
                # arr[next_index] >= 0 ensures we haven't visited it yet (unvisited values are non-negative)
                if 0 <= next_index < len(arr) and arr[next_index] >= 0:
                    queue.append(next_index)
      
        # No path to index with value 0 found
        return False
