# 땅따먹기

def solution(land):
    l = len(land)-1
    for i in range(l):
        land[i+1][0] += max(land[i][1],max(land[i][2],land[i][3]))
        land[i+1][1] += max(land[i][0],max(land[i][2],land[i][3]))
        land[i+1][2] += max(land[i][1],max(land[i][0],land[i][3]))
        land[i+1][3] += max(land[i][1],max(land[i][2],land[i][0]))

    answer = max(land[l][0],max(land[l][1],max(land[l][2],land[l][3])))
    return answer

# def solution(land):
#     answer = []
#     l = len(land)
#     def plus(avoid,result,now,goal):
#         if now > goal:
#             answer.append(result)
#             return
#         for idx,i in enumerate(land[now]):
#             if idx != avoid:
#                 plus(idx,result+i,now+1,goal)

#     for idx,i in enumerate(land[0]):
#         plus(idx,i,1,l-1)

#     return max(answer)