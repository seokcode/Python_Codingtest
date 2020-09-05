# 알파벳 # B_1987
# 백트래킹

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def go(board, check, x, y):
    n = len(board)
    m = len(board[0])
    ans = 0
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            # ord('A') -> A의 아스키코드 값 리턴
            ch = ord(board[nx][ny])-ord('A')
            if check[ch] == False:
                check[ch] = True
                temp = go(board, check, nx, ny)
                if ans < temp:
                    ans = temp
                check[ch] = False
    return ans+1

n,m = map(int,input().split())
board = [input() for _ in range(n)]
check = [False]*26
check[ord(board[0][0])-ord('A')] = True
print(go(board,check,0,0))

