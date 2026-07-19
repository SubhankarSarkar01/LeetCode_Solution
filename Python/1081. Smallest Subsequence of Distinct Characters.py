class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Create a dictionary to store the last occurrence index of each character
        last_occurrence = {char: index for index, char in enumerate(s)}
      
        # Stack to build the result string
        stack = []
      
        # Set to track which characters are already in the stack
        visited = set()
      
        # Iterate through each character in the string
        for index, char in enumerate(s):
            # Skip if character is already in our result
            if char in visited:
                continue
          
            # Remove characters from stack that are:
            # 1. Greater than current character (lexicographically)
            # 2. Will appear again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > index:
                removed_char = stack.pop()
                visited.remove(removed_char)
          
            # Add current character to stack and mark as visited
            stack.append(char)
            visited.add(char)
      
        # Join the stack to form the final result string
        return "".join(stack)
