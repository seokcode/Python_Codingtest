# Longest Palindromic Substring
> **Medium**
>
> **2021-04-08**
>
> **[Leetcode: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)**


## Sol
그리디로 풀려고 시도했지만..시간초과에 발목을 잡혀버려따..그래서 제일 알고리즘 효율이 좋다고 하는 풀이를 공부해보았다.  

   
for문 한바퀴 안에 문제는 답을 찾아낼 수 있다. 그 이유는 두개의 if문 때문인데,
```python
for j in range(len(s)):
    if s[j-l : j+1] == s[j-l : j+1][::-1]:
        i, l = j-l, l+1
    elif j-l > 0 and s[j-l-1 : j+1] == s[j-l-1 : j+1][::-1]:
        i, l = j-l-1, l+2
```
s='ebbc'라면 for문은 s의 길이만큼 탐색한다(1 <= s.length <= 1000).   
첫번째 if문은 순수하게 문자열의 앞에서부터 펠린드롬인지 확인해준다. `'e' == 'e'`인지, `'eb' == 'be'`인지,, 펠린드롬이 맞을경우 해당 인덱스를 기억하기 위해 i와 l에 저장해준다(i는 정답을 return해줄 때 쓰인다).  


방금 보았던 `'eb' == 'be'`는 펠린드롬이 아니다. 그렇기 때문에 첫번째 if문에 들어갈 수 없다. 그때부터는 두번째 if문을 돌게 되는데 두번째 if문은 j-l>0 이라는 조건이 있다.  
이 조건은 시작 인덱스를 0으로 하지 않겠다는 의미이다. 즉, 'ebbc'문자열의 경우 'bb'가 최종 답이 되는데 'bb'는 s[1:3]이므로 시작 인덱스가 0일 경우에는 도출할 수 없다. 이 경우를 위한 if문이다.  


그렇게 i,l은 점점 간격이 넓어지거나 유지되지 줄어들지 않기 때문에 최종적으로 for문이 다 돌고나서 i,l에 들어있는 인덱스 사이의 문자열이 가장 긴 펠린드롬이 된다. 


## 답안
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i , l =0 ,0
        for j in range(len(s)):
            if s[j-l : j+1] == s[j-l : j+1][::-1]:
                i, l = j-l, l+1

            elif j-l > 0 and s[j-l-1 : j+1] == s[j-l-1 : j+1][::-1]:
                i, l = j-l-1, l+2

        return s[i: i+l]
```

## 내 답안
> 틀린 내 풀이(테케통과 하지만 시간초과)  
> s에 900자가 들어오니까 시간초과가 나더라.. 1 <= s.length <= 1000
```python
from itertools import permutations as permu


class Solution:
    def longestPalindrome(self, s: str) -> str:
        numbers = [i for i in range(len(s))]
        answer = []

        def isPalindrome(test) -> bool:
            if test == test[::-1]:
                return True
            else:
                return False

        everything = permu(numbers, 2)
        new_evry = sorted(everything, key=lambda x: abs(x[0] - x[1]), reverse=True)

        for first, second in new_evry:
            if s[first:second + 1] != '':
                if isPalindrome(s[first:second + 1]):
                    return s[first:second + 1]

        return s[0]
```