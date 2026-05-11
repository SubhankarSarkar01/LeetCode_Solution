# -- 2553. Separate the Digits in an Array --
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        """
        Separates each integer in the input list into its individual digits.
      
        Args:
            nums: List of non-negative integers
          
        Returns:
            List containing all digits from the input numbers in order
        """
        result = []
      
        for number in nums:
            # Extract digits from current number
            digits_stack = []
          
            # Extract digits using modulo (gives digits in reverse order)
            while number > 0:
                digit = number % 10  # Get the last digit
                digits_stack.append(digit)
                number //= 10  # Remove the last digit
          
            # Add digits in correct order (reverse the stack)
            result.extend(digits_stack[::-1])
      
        return result
