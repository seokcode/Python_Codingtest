class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        empty = [[0]*n for _ in range(n)]
        visited = [[False]*n for _ in range(n)]
        dr, dc = [0,1,0,-1], [1,0,-1,0] # 오,아,왼,위
        r = c = di = 0 # (0,0)에서 시작. 방향도 오른쪽부터
        
        for i in range(1,(n*n)+1):
            empty[r][c] = i
            visited[r][c] = True
            nr, nc = r+dr[di], c+dc[di]
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                r, c= nr, nc
            else:
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
        return empty