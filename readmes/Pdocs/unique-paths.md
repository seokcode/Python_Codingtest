# Unique Paths
> **Medium**
>
> **2021-10-03**
>
> **[Leetcode: Unique Paths](https://leetcode.com/problems/unique-paths)**


## Sol
처음엔 아래처럼 BFS로 접근했지만 아무래도 모든 시작점에서 갈 수 있는 모든 경로를 조사해야하다보니 시간초과가 났다.
```python
from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        robot = [[0]*n for _ in range(m)]
        Q = deque([(0,0)])
        answer = 0
        
        while Q:
            x, y = Q.popleft()
            
            if x == m-1 and y == n-1:
                answer += 1
                
            if 0 <= x+1 < len(robot):
                Q.append((x+1,y))

            if 0 <= y+1 < len(robot[0]):
                Q.append((x,y+1))

        return answer
```

DP로 접근하려면 먼저 규칙을 찾아야한다. 로봇은 오른쪽과 아래 방향으로만 움직일 수 있다. 이 말은 다르게 보면 각 칸은 자신의 왼쪽과 위로부터 올 수 있다는 점이다.

따라서 각 칸 `dp[i][j]`으로 올 수 있는 방법의 수는 자신의 위(`dp[i - 1][j]`) + 자신의 왼쪽(`dp[i][j - 1]`) 방법의 수의 합과 같다.   
또한, 시작점 (0,0)을 기준으로 (0,0)~(0,N)까지와 (0,0)~(M,0)까지는 무조건 도달할 수 있는 곳이다.

|0|0|0|
|:--:|:--:|:--:|
|0|0|0|

⬇️

|1가지|1가지|1가지|
|:--:|:--:|:--:|
|1가지|2가지|`3가지`|


## 답안
> Runtime: 24 ms, faster than 96.66% of Python3 online submissions for Unique Paths.  
> Memory Usage: 14.4 MB, less than 38.21% of Python3 online submissions for Unique Paths.
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m-1][n-1]
```