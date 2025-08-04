# ---- 3028. Ant on the Boundary ----
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in nums:
            total +=i
            if total == 0:
                count +=1
            
        return count