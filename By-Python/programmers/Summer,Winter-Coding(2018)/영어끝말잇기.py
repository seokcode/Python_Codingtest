# 영어 끝말잇기

def solution(n, words):
    person = [0 for i in range(n)]
    storage = []
    for idx,w in enumerate(words):
        person[idx%n] += 1
        if storage:
            if storage[-1][-1] != w[0] or w in storage:
                return [(idx%n)+1, person[idx%n]]
        storage.append(w)
    
    return [0,0]