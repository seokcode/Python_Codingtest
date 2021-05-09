# 로또의 최고순위와 최저순위

def solution(lottos, win_nums):
    correct = 0
    zero = 0
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1: 6, 0: 6}
    for i in lottos:
        if i in win_nums:
            correct += 1
        elif i == 0:
            zero += 1
    
    return [rank[correct+zero], rank[correct]]