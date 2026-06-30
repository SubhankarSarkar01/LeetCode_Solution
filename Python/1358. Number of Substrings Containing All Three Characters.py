class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Dictionary to track the most recent index of each character
        # Initialize with -1 to indicate characters haven't been seen yet
        last_seen_index = {"a": -1, "b": -1, "c": -1}
      
        # Counter for valid substrings
        total_count = 0
      
        # Iterate through the string with index and character
        for current_index, char in enumerate(s):
            # Update the most recent index for the current character
            last_seen_index[char] = current_index
            min_index = min(last_seen_index["a"], last_seen_index["b"], last_seen_index["c"])
          
            total_count += min_index + 1
      
        return total_count
