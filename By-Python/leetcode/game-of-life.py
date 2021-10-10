class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:    
        N, M = len(board), len(board[0])
        nxtGen = [[False] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                live, dead = self.checkAroundMe(board,i,j)
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        nxtGen[i][j] = True
                elif board[i][j] == 0:
                    if live == 3:
                        nxtGen[i][j] = True
            
        for i in range(N):
            for j in range(M):
                if nxtGen[i][j]:
                    board[i][j] ^= 1
        
    def checkAroundMe(self, board, r, c):
        N, M = len(board), len(board[0])
        dx = [0,-1,-1,-1,0,1,1,1]
        dy = [-1,-1,0,1,1,1,0,-1]
        
        cntLive, cntDead = 0,0
        for d in range(8):
            nr, nc = r+dx[d], c+dy[d]
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1:
                    cntLive += 1
                else:
                    cntDead += 1
        
        return cntLive, cntDead
                    