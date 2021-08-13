# JadenCase 문자열 만들기
> **Lv2**
>
> **2021-06-20**
>
> [프로그래머스: 12951](https://programmers.co.kr/learn/courses/30/lessons/12951)


## Sol
### 문제 설명

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

### 예
`"3people unFollowed me"` => `"3people Unfollowed Me"`
`"for the last week"` => `"For The Last Week"`


여기서 주의해야할 점은 문자열을 그냥 나누는것이 아니라 " "(공백)을 기준으로 나누어야한다는 점이다.
"hello       world"와 같은 문자열이 있을 때, 답은 "Hello        World"가 되어야 하는데
s.split()을 하게 되면 ["hello","world"]가 되고 s.split(" ")을 하게되면 ['hello"," "," "," "," ","world"]로 되기 때문이다.

이 부분만 주의하여 정규식을 활용하여 단어의 맨 앞이 영소문자라면 맨 앞만 대문자로 바꿔주면 된다. 
 

## 답안
```python
import re

def solution(s):
    separateItem = s.split(" ") 
    answer = []
    for (idx,item) in enumerate(separateItem):
        if item == "":
            continue
            
        item = list(item.lower())
        if re.findall('[a-zA-Z]',item[0]):
            item[0] = item[0].upper()
        separateItem[idx] = "".join(item)
        
    return " ".join(separateItem)
```