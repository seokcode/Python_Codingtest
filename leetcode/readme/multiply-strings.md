# Multiply Strings
> **Medium**
>
> **2021-08-08**
>
> **[Leetcode: 43. Multiply Strings](https://leetcode.com/problems/multiply-strings)**


## Sol

주어지는 문자열 형태의 숫자를 서로 곱한 결과를 return해야하는 간단한 문제.

하지만 주어지는 문자열을 바로 정수형으로 변환해서는 안된다. 

0의 아스키 코드를 기준으로 아스키 코드 또한 1씩 증가한다는 점을 활용하여 아스키 코드 변환을 통해 문제를 풀어주었다.
> ord('0') = 48 / ord('1') = 49 ...


## 답안
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.makeInteger(num1) * self.makeInteger(num2))
        
    def makeInteger(self, str) -> int:
        result = 0
        for i in str:
            result *= 10
            result += (ord(i)-ord('0'))
            
        return result
```