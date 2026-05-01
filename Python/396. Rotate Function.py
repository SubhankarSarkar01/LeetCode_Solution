# -- 396. Rotate Function --
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Find the maximum value of rotation function F(k) for all k from 0 to n-1.
        F(k) = 0*arr[k] + 1*arr[k+1] + ... + (n-1)*arr[k+n-1]
        where arr[i] represents the rotated array.
        """
        # Calculate initial F(0) = 0*nums[0] + 1*nums[1] + ... + (n-1)*nums[n-1]
        current_rotation_value = sum(index * value for index, value in enumerate(nums))
      
        # Get array length and sum of all elements
        array_length = len(nums)
        total_sum = sum(nums)
      
        # Initialize maximum with F(0)
        max_rotation_value = current_rotation_value
      
        # Calculate F(1) through F(n-1) using the recurrence relation:
        # F(k) = F(k-1) + sum(nums) - n * nums[n-k]
        for rotation in range(1, array_length):
            # Update current rotation value using the formula
            # Adding total_sum adds 1 to each element's coefficient
            # Subtracting n * nums[n-rotation] corrects the last element that wraps to position 0
            current_rotation_value = current_rotation_value + total_sum - array_length * nums[array_length - rotation]
          
            # Track the maximum rotation value found so far
            max_rotation_value = max(max_rotation_value, current_rotation_value)
      
        return max_rotation_value
