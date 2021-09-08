# A->B
> **삼성 SW 역량 테스트 기출**
>
> **Silver 1**
>
> **2021-02-11**
>
> [B16953](https://www.acmicpc.net/problem/16953)


## Sol

BFS 혹은 그리디로도 풀 수 있는 문제였다.   
(BFS로 풀고나서 그리디 알고리즘도 적용해보았는데 그리디가 더 빨랐다.)  


<br>

문제에서 크게 고려해야 할 것은 3가지 경우이다.

**1. 2를 곱하기**  
**2. 최우측에 1을 추가하는 경우**  
**3.위 두가지 방법으로 b를 만들 수 없다면 -1을 출력한다**


<br>
 
## BFS 풀이
```python
from collections import deque

a,b = map(int, input().split())
q = deque()
q.append((a,1))
ans = -1

while q:
  a, cnt = q.popleft()

  if a == b:
    ans = cnt
    break
  
  if a*2 <= b:
    q.append((a*2, cnt+1))
  if int(str(a)+'1') <= b:
    q.append((int(str(a)+'1'), cnt+1))

print(ans)
```


## 그리디 풀이
> 그리디의 경우는 A->B가 아니라 B->A라고 생각하고 진행한다.

  
```python
a,b = map(int, input().split())
cnt = 1

while True:
  if b == a:
    break
  elif (b % 2 != 0 and b % 10 != 1) or (b < a):
    cnt = -1
    break
  else:
    if b % 10 == 1:
      b //= 10
      cnt += 1
    else:
      b //= 2
      cnt += 1
 
print(cnt)
```