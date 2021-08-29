# 플로이드-와샬
def solution(n, results):
    board = [["?" for _ in range(n)] for _ in range(n)]
    
    # 주어진 results 리스트를 토대로 각 선수별 자신을 제외한 나머지 선수와의 승패를 기록
    for a,b in results:
        board[a-1][b-1] = "WIN"
        board[b-1][a-1] = "LOSE"
    
    # 주어진 results를 토대로 확정지을 수 있는 승패를 판별
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 1. i와 j에 대한 승패가 아직 기록이 없는경우
                # 2-1. i가 k에게 승리하였고 j는 k에게 패배하였다면 i는 j보다 확실히 위에 있음
                # 2-2. i가 k에게 패배하였고 j는 k에게 승리하였다면 i는 j보다 확실히 아래 있음
                if board[i][j] == "?":
                    if board[i][k] == "WIN" and board[j][k] == "LOSE":
                        board[i][j] = "WIN"
                        board[j][i] = "LOSE" # 어차피 for문이 돌기 때문에 굳이 안해줘도 되지만 여기서 미리 처리 해준다면 for문이 한번 덜 돌겠지?
                        
                    elif board[i][k] == "LOSE" and board[j][k] == "WIN":
                        board[i][j] = "LOSE"
                        board[j][i] = "WIN"
    
    # 각 선수별로 자신을 제외한 나머지가 모두 1또는 -1로 승패가 판별됐다면 순위를 매길 수 있음(0이 자기 자신 하나만 있으면 됨)
    answer = 0
    for i in range(n):
        if board[i].count("?") == 1:
            answer += 1
            
    return answer