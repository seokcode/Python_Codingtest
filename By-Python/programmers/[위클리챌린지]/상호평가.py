def rotate(scores):
    N, M = len(scores), len(scores[0])
    turned = [[0] * N for _ in range(M)]
    
    for i in range(len(scores)):
        for j in range(len(scores[0])):
            turned[j][i] = scores[i][j]
        
    return turned

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
    
def solution(scores):
    answer = ''    
    tScores = rotate(scores)

    for idx,item in enumerate(tScores):
        if (max(item) == item[idx] or min(item) == item[idx]) and item.count(item[idx]) == 1:
            answer += grade((sum(item) - item[idx])/(len(item)-1))
        else:
            answer += grade(sum(item)/len(item))            
            
    return answer