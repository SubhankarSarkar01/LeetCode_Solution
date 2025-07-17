# --28. Find the Index of the First Occurrence in a String--



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            index = haystack.find(needle)
            return index
        return -1
        