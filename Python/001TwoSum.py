# QS : Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # -- Here Used unordered_map -- 
        num_map = {}
        for i, first in enumerate(nums):
            sec = target - first
            if sec in num_map:
                return [num_map[sec],i]

            num_map[first] = i
        return []
    
# --Time Complexity : O(n)
    
