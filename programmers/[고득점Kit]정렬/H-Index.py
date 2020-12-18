# H-Index

def solution(citations):
    answer = 0
    for i in range(0,max(citations)+1):
        num = 0
        for j in citations:
            if j >= i :
                num += 1
        if num >= i:
            answer = i

    return answer