# ----58. Length of Last Word----

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        rev = len(s) - 1
        while(rev>=0 and s[rev] == ' '): rev -=1
        while(rev>=0 and s[rev] != ' '):
            ans +=1
            rev -=1
        
        return ans
    
