# 크레인 인형뽑기 게임

def solution(board, moves):
    stack = [0]
    pick = list(map(lambda x: x - 1, moves))
    cnt = 0

    for pick_lane in pick:
        for i in range(len(board)):
            if board[i][pick_lane] != 0:
                stack.append(board[i][pick_lane])
                board[i][pick_lane] = 0

                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    cnt += 2
                break

    return cnt