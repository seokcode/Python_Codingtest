# 폴리오미노 # B_1343

board = input()
i = 0

while i < len(board):
    # 4글자를 스캔한 결과가 XXXX라면 AAAA로 대체
    if board[i:i+4] == 'XXXX':
        i += 4
        board = board.replace('X', 'A', 4)
    # 2글자를 스캔한 결과가 XX라면 BB로 대체
    elif board[i:i+2] == 'XX':
        i += 2
        board = board.replace('X', 'B', 2)
    # .일 경우 그대로 두고 스캔하는 글자만 넘겨줌
    elif board[i] == '.':
        i += 1
    else:
        board = -1
        break

print(board)