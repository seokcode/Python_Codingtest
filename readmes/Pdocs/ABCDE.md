# ABCDE
> **Gold 5**
>
> **2021-02-27**
>
> [B13023](https://www.acmicpc.net/problem/13023)


## Sol

문제의 요점은 A-B, B-C, C-D, D-E인 친구관계가 존재하는지를 조사하는 것이다.  
문제를 이해하는게 좀 어려웠는데 문제를 다시 설명하자면 다음과 같다
> 문제를 왜 이렇게 설명해놓는건지 모르겠다 도대체;  

2번 예제의 경우

|0|1| 
|:----:|:----:| 
|1|2|
|2|3|
|3|0|
|1|4| 

<img width=60% src=https://user-images.githubusercontent.com/42789819/109382272-dbe50380-7922-11eb-8afc-4077f5f7f149.jpg>

이러한 그림이 나오는데 무조건 A-B, B-C, C-D, D-E인 관계여야 하는 것이 아니라 **친구의 꼬리를 무는 관계가 4개**면 되는 문제였다. 
> Depth가 4이고 선형 관계이면 된다. 

그래서 내가 사용한 로직은 다음과 같다.
1. DFS 사용
2. 한번의 방문만 이루어져야하고 친구의 수(n) 만큼 visited 배열을 통해 방문했다면 True, 안했다면 False를 넣어준다
3. depth가 4가 되었다면 ans=True를 return한다  
(방문한 적이 없는 노드일 경우에만 depth+1하여 dfs를 재귀호출하게 됨으로 depth가 4가 되었다는 것은 4명의 꼬리를 문 관계가 완성되었다는 뜻이다.)


## 답안
```python
n, m = map(int, input().split())
visited = [False for _ in range(n)]
adj = [[] for _ in range(n)]

# 인접 리스트
for _ in range(m):
  a, b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a)

# DFS
def dfs(idx, depth):
    global ans
    visited[idx] = True
    if depth == 4:
      ans = True
      return
      
    for i in adj[idx]:
      if not visited[i]:
        dfs(i, depth+1)
        visited[i] = False

ans = False
for i in range(n):
  dfs(i, 0)
  visited[i] = False
  if ans:
    break

print(1 if ans else 0)
```