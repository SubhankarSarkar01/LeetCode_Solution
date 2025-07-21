# --151. Reverse Words in a String--

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_Words = words[::-1]
        result = ' '.join(reverse_Words)
        return result
        