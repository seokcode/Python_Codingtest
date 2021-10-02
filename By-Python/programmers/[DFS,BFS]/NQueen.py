def solution(n):
    check_x = [False] * n
    cross_sum = [False] * (n*2)
    cross_dis = [False] * (n*2)
    
    return nQueens(0, n, check_x, cross_sum, cross_dis)

def nQueens(q_cnt, N, check_x, cross_sum, cross_dis):
    cnt = 0
    
    if q_cnt == N:
        return 1
    
    for i in range(N):
        if check_x[i] or cross_sum[abs(i+q_cnt)] or cross_dis[i-q_cnt+N]:
            continue
        else:
            check_x[i] = True
            cross_sum[i+q_cnt] = True
            cross_dis[i-q_cnt+N] = True
            
            cnt += nQueens(q_cnt+1, N, check_x, cross_sum, cross_dis)
            
            check_x[i] = False
            cross_sum[i+q_cnt] = False
            cross_dis[i-q_cnt+N] = False
    
    return cnt