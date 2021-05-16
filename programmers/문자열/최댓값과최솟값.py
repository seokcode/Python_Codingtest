# 최댓값과 최솟값

def solution(s):
    answer = list(map(int,s.split()))
    return " ".join(list(map(str,[min(answer),max(answer)])))