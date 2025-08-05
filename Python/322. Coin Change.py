# ---- 322. Coin Change ----
class Solution:
    def solveRec(self,coins,amount,memo):
        if amount == 0:
            return 0
        
        if amount < 0:
            return float('inf')

        if amount in memo:
            return memo[amount]
        
        mini = float('inf')
        for i in range(len(coins)):
            ans = self.solveRec(coins,amount-coins[i],memo)
            if ans !=float('inf'):
                mini = min(mini,1+ans)
        memo[amount] = mini
        return mini

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        ans = self.solveRec(coins,amount,memo)
        if ans == float('inf'):
            return -1
        else:
            return ans
        
        