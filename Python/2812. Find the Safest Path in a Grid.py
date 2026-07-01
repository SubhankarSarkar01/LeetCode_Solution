from collections import deque
from typing import List
from itertools import pairwise
from math import inf


class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression and union by size."""

    def __init__(self, n: int) -> None:
        """Initialize Union-Find with n elements."""
        self.parent = list(range(n))  # Each element is initially its own parent
        self.size = [1] * n  # Size of each component

    def find(self, x: int) -> int:
        """Find the root of element x with path compression."""
        if self.parent[x] != x:
            # Path compression: make x point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """
        Union two elements a and b.
        Returns True if they were in different sets, False if already connected.
        """
        root_a, root_b = self.find(a), self.find(b)

        if root_a == root_b:
            return False  # Already in the same set

        # Union by size: attach smaller tree to larger tree
        if self.size[root_a] > self.size[root_b]:
            self.parent[root_b] = root_a
            self.size[root_a] += self.size[root_b]
        else:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]

        return True


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Find the maximum safeness factor for a path from (0,0) to (n-1,n-1).
        Safeness factor is the minimum distance to any thief along the path.
        """
        n = len(grid)

        # If start or end position has a thief, no safe path exists
        if grid[0][0] or grid[n - 1][n - 1]:
            return 0

        # Step 1: Calculate minimum distance from each cell to nearest thief using BFS
        queue = deque()
        distance_to_thief = [[inf] * n for _ in range(n)]

        # Initialize queue with all thief positions
        for row in range(n):
            for col in range(n):
                if grid[row][col]:  # Found a thief
                    queue.append((row, col))
                    distance_to_thief[row][col] = 0

        # Four directions: up, right, down, left
        directions = (-1, 0, 1, 0, -1)

        # BFS to calculate distances
        while queue:
            curr_row, curr_col = queue.popleft()

            # Check all four adjacent cells
            for delta_row, delta_col in pairwise(directions):
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col

                # Check if the next cell is valid and hasn't been visited
                if (0 <= next_row < n and
                    0 <= next_col < n and
                    distance_to_thief[next_row][next_col] == inf):

                    distance_to_thief[next_row][next_col] = distance_to_thief[curr_row][curr_col] + 1
                    queue.append((next_row, next_col))

        # Step 2: Sort all cells by their distance to thieves (descending order)
        cells_by_distance = []
        for row in range(n):
            for col in range(n):
                cells_by_distance.append((distance_to_thief[row][col], row, col))

        cells_by_distance.sort(reverse=True)

        # Step 3: Use Union-Find to connect cells, starting from highest distance
        union_find = UnionFind(n * n)

        for distance, row, col in cells_by_distance:
            # Try to connect current cell with adjacent cells of same or higher distance
            for delta_row, delta_col in pairwise(directions):
                next_row = row + delta_row
                next_col = col + delta_col

                if (0 <= next_row < n and
                    0 <= next_col < n and
                    distance_to_thief[next_row][next_col] >= distance):

                    # Connect cells using 1D indexing: row * n + col
                    union_find.union(row * n + col, next_row * n + next_col)

            # Check if start and end are connected
            start_index = 0  # (0, 0) -> 0
            end_index = n * n - 1  # (n-1, n-1) -> n*n - 1

            if union_find.find(start_index) == union_find.find(end_index):
                return int(distance)

        return 0
