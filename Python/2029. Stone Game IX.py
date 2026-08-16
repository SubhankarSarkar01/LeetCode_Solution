class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def can_alice_win(count: List[int]) -> bool:
            """
            Check if Alice can win with a specific starting strategy.
            Alice starts by picking a stone with value % 3 == 1.
          
            Args:
                count: List where count[i] represents stones with value % 3 == i
          
            Returns:
                True if Alice can win with this strategy
            """
            # If no stones with remainder 1, Alice cannot start with this strategy
            if count[1] == 0:
                return False
          
            # Alice picks a stone with remainder 1 first
            count[1] -= 1
          
            # Calculate total moves in the game
            # Start with 1 (Alice's first move)
            # Add pairs of remainder 1 and 2 stones (each pair contributes 2 moves)
            # Add all remainder 0 stones (they don't change the sum mod 3)
            total_moves = 1 + min(count[1], count[2]) * 2 + count[0]
          
            # If there are extra remainder 1 stones after pairing
            if count[1] > count[2]:
                count[1] -= 1
                total_moves += 1
          
            # Alice wins if:
            # 1. Total moves is odd (Bob runs out of valid moves)
            # 2. The remaining stones don't leave Bob in a winning position
            return total_moves % 2 == 1 and count[1] != count[2]
      
        # Count stones by their remainder when divided by 3
        remainder_count = [0] * 3
        for stone in stones:
            remainder_count[stone % 3] += 1
      
        # Try two strategies for Alice:
        # Strategy 1: Start with a stone where value % 3 == 1
        strategy_one = [remainder_count[0], remainder_count[1], remainder_count[2]]
      
        # Strategy 2: Start with a stone where value % 3 == 2
        strategy_two = [remainder_count[0], remainder_count[2], remainder_count[1]]
      
        # Alice wins if either strategy works
        return can_alice_win(strategy_one) or can_alice_win(strategy_two)
