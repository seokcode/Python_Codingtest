# Reverse Words in a String III
> **Easy**
>
> **2021-11-14**
>
> **[Leetcode: Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)**


## Sol

주어진 문자열 내 단어들을 전부 뒤집는 문제  
> Input: s = "Let's take LeetCode contest"  
> Output: "s'teL ekat edoCteeL tsetnoc"

## 답안
> Runtime: 32 ms, faster than 86.32% of Python3 online submissions for Reverse Words in a String III.  
> Memory Usage: 14.8 MB, less than 62.77% of Python3 online submissions for Reverse Words in a String III.
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        split_list = [i[::-1] for i in split_list]
        return " ".join(split_list)
```