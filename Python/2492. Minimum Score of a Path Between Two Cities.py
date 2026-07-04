from collections import defaultdict
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Build adjacency list representation of the undirected graph
        graph = defaultdict(list)
        for node_a, node_b, distance in roads:
            # Add edge in both directions since it's undirected
            graph[node_a].append((node_b, distance))
            graph[node_b].append((node_a, distance))
      
        # Track visited nodes to avoid cycles during DFS
        visited = [False] * (n + 1)  # Index 0 unused, nodes are 1-indexed
      
        # Initialize minimum score to infinity
        min_score = float('inf')
      
        def depth_first_search(current_node):
            """
            Perform DFS to explore all nodes in the connected component
            and find the minimum edge weight.
          
            Args:
                current_node: Current node being explored
            """
            nonlocal min_score
          
            # Check all edges from current node
            for neighbor, edge_weight in graph[current_node]:
                # Update minimum score if we found a smaller edge weight
                min_score = min(min_score, edge_weight)
              
                # Continue DFS if neighbor hasn't been visited
                if not visited[neighbor]:
                    visited[neighbor] = True
                    depth_first_search(neighbor)
      
        # Start DFS from node 1
        visited[1] = True
        depth_first_search(1)
      
        return min_score
