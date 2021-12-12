# Valid Parentheses
> **Easy**
>
> **2021-12-12**
>
> **[Leetcode: Valid Parentheses](https://leetcode.com/problems/valid-parentheses)**


## Sol
 
(, {, [ 괄호가 각각 ), }, ] 와 짝을 이루는지 올바른 괄호형식인지 판별하는 문제이다. 스택을 사용하였다.

## 답안
> Runtime: 28 ms, faster than 87.18% of Python3 online submissions for Valid Parentheses.  
> Memory Usage: 14.3 MB, less than 36.61% of Python3 online submissions for Valid Parentheses.
```python
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        
        for item in s:
            if item == "(" or item == "{" or item == "[":
                brackets.append(item)
            else:
                if brackets:
                    if item == ")" and brackets[-1] == "(":
                        brackets.pop()
                    elif item == "}" and brackets[-1] == "{":
                        brackets.pop()
                    elif item == "]" and brackets[-1] == "[":
                        brackets.pop()
                    else:
                        return False
                else:
                    return False
        
        if not brackets:
            return True
        else:
            return False
```
---

> 다른방법(딕셔너리 활용)  
>
> Runtime: 36 ms, faster than 32.19% of Python3 online submissions for Valid Parentheses.  
> Memory Usage: 14.4 MB, less than 7.96% of Python3 online submissions for Valid Parentheses.
```python
class Solution(object):
    def isValid(self, s):
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3
	
    # 1. if it's the left bracket then we append it to the stack
    # 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
    # 3. finally check if the stack still contains unmatched left bracket
```