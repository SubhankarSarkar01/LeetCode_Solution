# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j < len(t):
            if i == len(s):
                break
            elif s[i] == t[j]:
                i +=1
                j +=1
            else:
                j +=1
            
        return i == len(s)