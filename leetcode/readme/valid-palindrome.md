# Valid Palindrome
> **Easy**
>
> **2021-04-07**
>
> **[Leetcode: Valid-Palindrome](https://leetcode.com/problems/valid-palindrome)**


## Sol
펠린드롬이란 'bob'처럼 앞,뒤가 똑같은 문자열을 말한다.  
주어지는 문자열은 영문,숫자로만 이루어져있기 때문에 소문자로 변환한 뒤, 정규식검사를 통해 영문,숫자들만 찾고 join함수와 lower함수를 통해 합쳐주었다.  
길이가 1인 경우에는 모두 다 펠린드롬이 성립하므로 True를 반환 해주고, 길이가 n인 경우에는 (s[0],s[n-1]), (s[1],s[n-1-1])...와 같이 같아야하므로  
하나라도 다르다면 False를 return해주었다.


## 답안
```python
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= re.findall('[a-zA-Z0-9+]',s)
        s = ''.join(s).lower()
        if len(s) == 1:
            return True
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
            
        return True
            
        
```