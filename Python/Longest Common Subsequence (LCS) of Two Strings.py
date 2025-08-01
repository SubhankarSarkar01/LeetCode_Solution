# ---- Longest Common Subsequence (LCS) of Two Strings ----
class Solution:
    def solve(self,a, b, i, j, dp):
        if i == len(a):
            return 0

        if j == len(b):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        ans = 0
        if a[i] == b[j]:
            ans = 1 + self.solve(a ,b ,i+1 , j+1, dp)
        else:
            ans = max(self.solve(a,b,i+1,j,dp), self.solve(a,b,i,j+1,dp))

        dp[i][j] = ans
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for i in range(len(text1)):
            row = []
            for j in range(len(text2)):
                row.append(-1)
            dp.append(row)
        
        return self.solve(text1, text2, 0, 0, dp)
        