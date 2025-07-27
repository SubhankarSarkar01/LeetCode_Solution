# -- 26. Remove Duplicates from Sorted Array --

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for x in nums:
            if k == 0 or nums[k-1] !=x:
                nums[k] = x
                k +=1
        
        return k
        