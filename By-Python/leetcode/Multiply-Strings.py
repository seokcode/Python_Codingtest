class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.makeInteger(num1) * self.makeInteger(num2))
        
    def makeInteger(self, str) -> int:
        result = 0
        for i in str:
            result *= 10
            result += (ord(i)-ord('0'))
            
        return result