# ---- 69. Sqrt(x) ----
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1,x
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2

            if mid <= x//mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return ans