from collections import deque
from typing import List
from math import inf
from itertools import pairwise


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
      
        # Initialize distance matrix with infinity
        # distance[i][j] represents minimum cost to reach cell (i, j)
        distance = [[inf] * cols for _ in range(rows)]
      
        # Starting cell cost is the value of grid[0][0]
        distance[0][0] = grid[0][0]
      
        # Initialize BFS queue with starting position
        queue = deque([(0, 0)])
      
        # Direction vectors for moving up, right, down, left
        # Using pairwise will create: (-1, 0), (0, 1), (1, 0), (0, -1)
        directions = (-1, 0, 1, 0, -1)
      
        # BFS to find minimum cost path
        while queue:
            current_x, current_y = queue.popleft()
          
            # Explore all 4 adjacent cells
            for delta_x, delta_y in pairwise(directions):
                next_x = current_x + delta_x
                next_y = current_y + delta_y
              
                # Check if next position is valid and if we found a better path
                if (0 <= next_x < rows and 
                    0 <= next_y < cols and 
                    distance[next_x][next_y] > distance[current_x][current_y] + grid[next_x][next_y]):
                  
                    # Update minimum cost to reach this cell
                    distance[next_x][next_y] = distance[current_x][current_y] + grid[next_x][next_y]
                  
                    # Add this cell to queue for further exploration
                    queue.append((next_x, next_y))
      
        # Check if we can reach bottom-right corner with health remaining
        return distance[-1][-1] < health
