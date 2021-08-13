# 삼각 달팽이

import itertools

def snailNext(x,y,d_snail) :
    if d_snail %3 ==0 : # 아래
        x+=1
    elif d_snail %3 ==1 : # 우측
        y+=1
    else :
        x-=1
        y -=1
    return x,y

def solution(n):
    tri_snail = [[0 for k in range(1,i+1)] for i in range(1,n+1) ]
    direct_snail = range(n)  # 0부터 n 까지의 리스트
    x, y= -1, 0
    idx = 1
    for d_snail in direct_snail :  # 0 일때 아래,  1일때 오른쪽, 2일때 위
        for i in range(d_snail, n) :
            x,y = snailNext(x,y,d_snail)
            tri_snail[x][y]= idx
            idx+=1
    return list(itertools.chain(*tri_snail))