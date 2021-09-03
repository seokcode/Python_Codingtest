from itertools import permutations as permu
from collections import deque


def check(banned, candidates):
    for candi in candidates:
        ban = banned.popleft()
        if len(candi) == len(ban):
            for idx,b in enumerate(ban):
                    if b == "*":
                        continue
                    if b != candi[idx]:
                        return False
        else: 
            return False
    
    return True

def solution(user_id, banned_id):
    
    banCandidate = map(list,permu(user_id, len(banned_id)))
    answer = []
    
    for candidates in banCandidate:
        banned = deque(banned_id)
        if check(banned, candidates):
            if set(candidates) not in answer:
                answer.append(set(candidates))
            
    return len(answer)