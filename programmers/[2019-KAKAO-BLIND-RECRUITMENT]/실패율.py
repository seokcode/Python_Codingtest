# 실패율

def solution(N, stages):
    failure = []
    people = len(stages)
    for i in range(N):
        fail = stages.count(i+1)
        if fail == 0:
            failure.append([i,0])
        else:
            failure.append([i,(fail/people)])
        people -= fail        
    
    failure = sorted(failure, key=lambda x: (-x[1],x[0]))
    return [i[0]+1 for i in failure]