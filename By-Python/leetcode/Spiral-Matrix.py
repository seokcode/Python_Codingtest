class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        R, C = len(matrix), len(matrix[0])        
        visited = [[False]*C for _ in range(R)]
        dr, dc = [0,1,0,-1], [1,0,-1,0] # 오,아,왼,위
        result = []
        r = c = di = 0
        
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