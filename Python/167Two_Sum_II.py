# QS : Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        start, end  = 0, len(numbers)-1
        while(start<end):
            summ = numbers[start] + numbers[end]
            if target < summ:
                end -=1
            elif target > summ:
                start +=1
            else:
                return [start+1,end+1]
            
        return []

        