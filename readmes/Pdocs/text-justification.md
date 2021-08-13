# Text Justification
> **Hard**
>
> **2021-08-08**
>
> **[Leetcode: Text Justification](https://leetcode.com/problems/text-justification/)**


## Sol 

로직은 짰지만 구현에 있어서 시간이 걸렸던 다소 까다로운 문제.

문제에서 요구하는 조건은 다음과 같았다.

* 단어가 담긴 주어진 배열에서 단어를 순서대로 합쳐 문장으로 만든다.

* 단, 단어가 추가 되었을 때 주어진 maxWidth를 넘어가게 되면 그 단어는 다음 라인(줄)으로 넘긴다.

* 그리고 현재 라인에 포진된 단어들 사이의 공백을 균등 배분하여 삽입함으로써 maxWidth의 길이로 맞춘다.

* 균등 배분이 안된다면 왼쪽부터 남는 빈칸을 채워준다(5를 3등분 해야한다면 2,2,1)

* 마지막 라인은 공백의 균등 배분을 시행하지 않고 무조건 단어와 단어 사이는 한 칸만 띄운다. maxWidth를 맞추기 위한 빈칸은 문장의 끝부분에 삽입한다.


## 답안
```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line, allLines = [], []
        curlen = 0
        for idx in range (len(words)):
            # 1. 현재 단어까지 더하면 최대치를 넘어갈 경우
            if curlen + len(words[idx]) + len(line) > maxWidth:
                # 문장 꾸리기
                self.addline(line, allLines, maxWidth-curlen)
                
                # 초기화
                line = []
                
                # 현재 단어는 문장꾸리기에 포함되지 않았기 때문에 다음 for문을 위해 추가
                line.append(words[idx])
                curlen = len(words[idx])
                
                # 근데 해당 단어가 words배열의 마지막 단어였을 경우 바로 문장 꾸리기로 넘겨
                # 이 경우는 단어가 하나만 존재하는 경우
                if idx == len(words)-1:
                    self.addline(line, allLines, maxWidth-curlen)
           
            # 2. 현재 단어까지 더해도 최대치 이하인 경우
            else:
                line.append(words[idx])
                curlen += len(words[idx])
                
                # 최대치는 이하이지만 그 단어가 words 배열의 마지막 단어였다면 문장 꾸리기로 넘겨야함
                # 이 경우는 단어가 여러개 존재하는 경우 -> 단어와 단어 사이는 한칸만 나머지는 끝나는 단어 우측에 삽입
                if idx == len(words)-1:
                    new = ''
                    for i in range (len(line)-1):
                        new += line[i] + ' '
                    new+=line[-1]
                    new+= ' '*((maxWidth)-len(new))
                    allLines.append(new)
        return allLines
                    
    # maxWidth에 맞춰서 문장을 꾸리는 메서드
    def addline(self, l, allLines, space):
        # divide by zero 처리
        left = space//(len(l)-1) if len(l)>1 else space//len(l)
        over = space%(len(l)-1)  if len(l)>1 else space%len(l)
        line = ''
        
        for i in range (len(l)):
            line += l[i]
            if len(l)==1 or i<len(l)-1:
                line += ' '*left
                
                # 나머지가 있다는 것은 왼쪽에 더 많은 space를 넣어야 하는 것
                # 5//3 = 1 && 5%3 = 2이다. 이 말은 모두 1칸씩 갖되 왼쪽부터 1칸씩 추가로 가져야 한다는 뜻이다.
                # 따라서 2, 2, 1 순으로 space가 분배된다. 아래는 그 로직이다.
                if over>0:
                    line+= ' '
                    over-=1
        allLines.append(line)
```