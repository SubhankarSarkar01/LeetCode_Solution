class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        """
        Distribute elements from nums into two arrays based on comparison of their last elements.
      
        Args:
            nums: List of integers to be distributed
          
        Returns:
            Concatenated result of the two arrays
        """
        # Initialize first array with the first element
        arr1 = [nums[0]]
      
        # Initialize second array with the second element
        arr2 = [nums[1]]
      
        # Iterate through remaining elements starting from index 2
        for current_element in nums[2:]:
            # If last element of arr1 is greater than last element of arr2
            if arr1[-1] > arr2[-1]:
                # Add current element to arr1
                arr1.append(current_element)
            else:
                # Otherwise, add current element to arr2
                arr2.append(current_element)
      
        # Return concatenation of both arrays
        return arr1 + arr2
