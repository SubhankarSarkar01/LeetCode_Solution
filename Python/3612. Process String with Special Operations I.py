class Solution:
    def processStr(self, s: str) -> str:
        result = [] 
      
        for char in s:
            if char.isalpha():
                result.append(char)
            elif char == "*" and result:
                result.pop()
            elif char == "#":
                result.extend(result[:]) 
            elif char == "%":
                result.reverse()
        return "".join(result)
