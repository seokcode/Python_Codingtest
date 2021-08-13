# 프로그래머스 고득점 Kit K번째 수

def solution(array, commands):
    answer = []

    for num in commands:
        newarray = array[num[0] - 1:num[1]]
        newarray.sort()
        answer.append(newarray[num[2] - 1])

    return answer

# 한줄 풀이
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))