# -- 35. Search Insert Position--
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0 ,len(nums)-1
        while start <=end:
            mid = (start + end) //2
            if nums[mid] < target:
                start = mid + 1
            else :
                end = mid -1
            
        return start
    