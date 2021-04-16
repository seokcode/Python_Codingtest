# 음양더하기

def solution(absolutes, signs):
    answer = 0
    d = zip(absolutes, signs)
    
    for a,b in d:
        if b: answer += a 
        else: answer -= a
    
    return answer