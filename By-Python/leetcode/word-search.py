class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        goal = list(word)
        visit = [[False] * len(board[0]) for _ in range(len(board))]
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == goal[0]:
                    visit[row][col] = True # visit
                    if self.findWord(visit, board, row, col, 1, goal):
                        return True
                    visit[row][col] = False # recover
                    
        return False
    
    def findWord(self, visit, board, row, col, idx, goal):
        ROW, COL = len(board), len(board[0])
        dx = [0,-1,0,1]
        dy = [1,0,-1,0]
        
        # found word
        if idx == len(goal):
            return True
        
        for d in range(4):
            nx = row+dx[d]
            ny = col+dy[d]
            # next location exists in range
            if 0 <= nx < ROW and 0 <= ny < COL:
                # next location is valid character && visit not yet
                if board[nx][ny] == goal[idx] and not visit[nx][ny]:
                    visit[nx][ny] = True # visit
                    if self.findWord(visit, board, nx, ny, idx+1, goal): 
                        return True
                    visit[nx][ny] = False # recover
                
        return False 