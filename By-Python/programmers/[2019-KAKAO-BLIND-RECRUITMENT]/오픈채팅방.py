# 오픈채팅방

from collections import defaultdict
def solution(record):
    answer = []
    d = defaultdict(list)
    
    for i in record:
        temp = i.split()
        if temp[0] == "Change" or temp[0] == "Enter":
            d[temp[1]] = temp[2]
        
        if temp[0] == "Enter":
            temp[0] = "님이 들어왔습니다."
            answer.append([temp[1],temp[0]])
        elif temp[0] == "Leave":
            temp[0] = "님이 나갔습니다."
            answer.append([temp[1],temp[0]])
    
    
    for j in range(len(answer)): 
        answer[j][0] = d[answer[j][0]]
        answer[j] = ''.join(answer[j])

    return answer