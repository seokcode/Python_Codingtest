# Spiral Matrix
> **Medium**
>
> **2021-08-01**
>
> **[Leetcode: Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)**


## Sol

이런 문제를 만날때마다 풀릴 것 같으면서 이상하게 꼬였는데 너무 어렵게 생각해왔던 것 같다.

먼저 파악해야하는 사항은 이렇다.
1. 방향은 총 4가지이다. 그리고 (오른,아래,왼쪽,위)의 순서가 반복된다(방향의 순서가 정해져있다).
2. 몇번 꺾이는지는 규칙적이지 않다.
3. 하지만 끝에 도달했거나 이미 방문한 곳을 만나면 방향이 전환된다.
4. 마지막 숫자는 가로x세로의 결과이다(ex 4x3 사각형이면 12가 마지막 숫자).


이를 바탕으로 로직을 설계한다.


## 답안
> Runtime: 32 ms, faster than 63.01% of Python3 online submissions for Spiral Matrix.  
> Memory Usage: 14.1 MB, less than 83.56% of Python3 online submissions for Spiral Matrix.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        R, C = len(matrix), len(matrix[0])        
        visited = [[False]*C for _ in range(R)]
        dr, dc = [0,1,0,-1], [1,0,-1,0] # 오,아,왼,위
        result = []
        r = c = di = 0 # (0,0)에서 시작. 방향도 오른쪽부터
        
        for _ in range(R * C):
            result.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r+dr[di], c+dc[di]
            
            # 다음 목적지가 장외가 아니고 방문한 적 없는 곳이라면 방문하기
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                r, c = nr, nc
            # 아니라면 방향 전환하기
            else:
                # 방향은 총 4가지
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return result
```