class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # Create a mutable copy of restrictions to avoid modifying the input
        height_restrictions = restrictions.copy()
      
        # Add the starting position: building 1 must have height 0
        height_restrictions.append([1, 0])
      
        # Sort restrictions by position
        height_restrictions.sort()
      
        # Add the last position if not already present
        # The maximum possible height at position n is n-1 (starting from 0 at position 1)
        if not height_restrictions or height_restrictions[-1][0] != n:
            height_restrictions.append([n, n - 1])
      
        num_restrictions = len(height_restrictions)
      
        # Forward pass: propagate height constraints from left to right
        # Each building's height is limited by the previous building's height plus the distance
        for i in range(1, num_restrictions):
            max_height_from_left = height_restrictions[i - 1][1] + (height_restrictions[i][0] - height_restrictions[i - 1][0])
            height_restrictions[i][1] = min(height_restrictions[i][1], max_height_from_left)
      
        # Backward pass: propagate height constraints from right to left
        # Each building's height is also limited by the next building's height plus the distance
        for i in range(num_restrictions - 2, 0, -1):
            max_height_from_right = height_restrictions[i + 1][1] + (height_restrictions[i + 1][0] - height_restrictions[i][0])
            height_restrictions[i][1] = min(height_restrictions[i][1], max_height_from_right)
      
        # Find the maximum possible height between consecutive restriction points
        max_height = 0
        for i in range(num_restrictions - 1):
            # Calculate the maximum height that can be achieved between two consecutive points
            # The formula finds the peak height when growing from both endpoints
            left_height = height_restrictions[i][1]
            right_height = height_restrictions[i + 1][1]
            distance = height_restrictions[i + 1][0] - height_restrictions[i][0]
          
            # Maximum height between two points with given endpoint heights
            peak_height = (left_height + right_height + distance) // 2
            max_height = max(max_height, peak_height)
      
        return max_height
