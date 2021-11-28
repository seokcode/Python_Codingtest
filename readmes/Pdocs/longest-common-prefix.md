# Longest Common Prefix
> **Easy**
>
> **2021-11-28**
>
> **[Leetcode: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)**


## Sol
주어진 단어 배열에서 가장 길게 공통되는 접두사를 찾는 문제.

## 답안
> Runtime: 32 ms, faster than 84.09% of Python3 online submissions for Longest Common Prefix.  
> Memory Usage: 14.3 MB, less than 81.98% of Python3 online submissions for Longest Common Prefix.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 주어진 배열에서 가장 짧은 단어를 찾는다.
        # 어차피 최대 길이의 접두사는 짧은 단어의 길이를 못넘기 때문.
        shortestWord = min(strs,key=len)
        
        # 그 단어 내의 글자를 하나씩 비교하면서 다른 단어들과 차이를 보이는 지점을 찾는다. 
        # 그 지점 미만까지가 최대 접두어가 된다.
        for i, ch in enumerate(shortestWord):
            for other in strs:
                if other[i] != ch:
                    return shortestWord[:i]
        return shortestWord 
```