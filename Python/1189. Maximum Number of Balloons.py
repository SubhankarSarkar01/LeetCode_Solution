from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count frequency of each character in the input text
        char_count = Counter(text)
      
        # 'balloon' has 1 'b', 1 'a', 2 'l's, 2 'o's, 1 'n'
        # Divide count of 'l' and 'o' by 2 since we need 2 of each per 'balloon'
        char_count['o'] //= 2
        char_count['l'] //= 2
      
        # Find the minimum count among required characters
        # This determines the maximum number of 'balloon' words we can form
        return min(char_count[c] for c in 'balon')
