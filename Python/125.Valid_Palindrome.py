# -- 125. Valid Palindrome -- 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st, end  = 0, len(s)-1
        while(st < end):
            if not s[st].isalnum():
                st +=1
                continue
            elif not s[end].isalnum():
                end -=1
                continue
            elif s[st].lower() != s[end].lower():
                return False
            
            st +=1
            end -=1

        return True
    
# Time Complexity : O(n)
            
        
