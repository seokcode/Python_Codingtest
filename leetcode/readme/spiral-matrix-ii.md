# Spiral Matrix II
> **Medium**
>
> **2021-08-01**
>
> **[Leetcode: Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)**


## Sol
Spiral Matrix I과 다른 점
1. n만 주어진다
2. 무조건 n x n의 정사각형이다
3. 일차원배열을 return하는게 아니라 matrix(사각형 설계도)를 return한다.

먼저 파악해야하는 사항은 I과 똑같다.
1. 방향은 총 4가지이다. 그리고 (오른,아래,왼쪽,위)의 순서가 반복된다(방향의 순서가 정해져있다).
2. 몇번 꺾이는지는 규칙적이지 않다.
3. 하지만 끝에 도달했거나 이미 방문한 곳을 만나면 방향이 전환된다.
4. 마지막 숫자는 n*n이다.

이를 바탕으로 로직을 설계한다.

## 답안
> Runtime: 28 ms, faster than 88.53% of Python3 online submissions for Spiral Matrix II.  
> Memory Usage: 14.4 MB, less than 47.55% of Python3 online submissions for Spiral Matrix II.

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        empty = [[0]*n for _ in range(n)]
        visited = [[False]*n for _ in range(n)]
        dr, dc = [0,1,0,-1], [1,0,-1,0] # 오,아,왼,위
        r = c = di = 0 # (0,0)에서 시작. 방향도 오른쪽부터
        
        # 마지막 숫자는 n*n이므로 1~n*n으로 범위지정
        for i in range(1,(n*n)+1):
            empty[r][c] = i
            visited[r][c] = True
            nr, nc = r+dr[di], c+dc[di]
            
            # 다음 목적지가 장외가 아니고 방문한 적 없는 곳이라면 방문하기
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                r, c= nr, nc
            # 아니라면 방향 전환하기
            else:
                # 방향은 총 4가지
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return empty
```