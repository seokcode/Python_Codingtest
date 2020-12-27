# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    a = list(skill)

    for i in skill_trees:
        i = list(i)
        temp = []
        for j in range(len(i)):
            for k in range(len(a)):
                if i[j] == a[k]:
                    temp.append(i[j])
        if ''.join(temp) == skill[:len(temp)]:
            answer += 1

    return answer