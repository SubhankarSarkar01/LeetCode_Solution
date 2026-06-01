class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Sort the array in descending order to prioritize buying expensive items first
        cost.sort(reverse=True)
      
        # Calculate total cost minus every third item (which is free)
        # cost[2::3] gets every third item starting from index 2 (0-indexed)
        # This implements the "buy 2 get 1 free" offer optimally
        total_cost = sum(cost) - sum(cost[2::3])
      
        return total_cost
