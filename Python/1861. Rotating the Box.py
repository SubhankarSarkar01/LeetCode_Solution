# 1861. Rotating the Box

from collections import deque
from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Get dimensions of the original box
        rows, cols = len(box), len(box[0])
      
        # Create rotated box with swapped dimensions
        # After 90° clockwise rotation: new_rows = original_cols, new_cols = original_rows
        rotated_box = [[None] * rows for _ in range(cols)]
      
        # Perform 90 degree clockwise rotation
        # Original position (i, j) maps to (j, rows - 1 - i) after rotation
        for row in range(rows):
            for col in range(cols):
                rotated_box[col][rows - row - 1] = box[row][col]
      
        # Apply gravity to make stones fall down in the rotated box
        # Process each column independently
        for col in range(rows):
            # Queue to track available empty positions where stones can fall
            empty_positions = deque()
          
            # Process from bottom to top (gravity pulls stones down)
            for row in range(cols - 1, -1, -1):
                if rotated_box[row][col] == '*':
                    # Obstacle found - clear empty positions queue
                    # Stones cannot fall past obstacles
                    empty_positions.clear()
                elif rotated_box[row][col] == '.':
                    # Empty space found - add to available positions
                    empty_positions.append(row)
                elif rotated_box[row][col] == '#' and empty_positions:
                    # Stone found with empty space below - make it fall
                    # Move stone to the lowest available empty position
                    lowest_empty = empty_positions.popleft()
                    rotated_box[lowest_empty][col] = '#'
                    rotated_box[row][col] = '.'
                    # Current position becomes empty after stone falls
                    empty_positions.append(row)
      
        return rotated_box
