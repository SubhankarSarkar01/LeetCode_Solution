# 3151. Special Array I
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        def parity(num):
            if num %2 == 1:
                return 'odd'
            else:
                return 'even'
            
        for i in range(1,len(nums)):
            if parity(nums[i]) == parity(nums[i-1]):
                return False
            
        return True