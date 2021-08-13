# 정수 삼각형

import copy

def solution(triangle):
    d = copy.deepcopy(triangle)
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            if triangle[i+1][j] + d[i][j] > d[i+1][j]:
                d[i+1][j] = triangle[i+1][j] + d[i][j]
            
            if triangle[i+1][j+1] + d[i][j] > d[i+1][j+1]:
                d[i+1][j+1] = triangle[i+1][j+1] + d[i][j]
    
    return max(d[len(d)-1])


import copy

def solution(triangle):    
    d = copy.deepcopy(triangle)
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            d[i+1][j] = max(triangle[i+1][j] + d[i][j], d[i+1][j])
            d[i+1][j+1] = max(triangle[i+1][j+1] + d[i][j], d[i+1][j+1])

    return max(d[len(d)-1])\
