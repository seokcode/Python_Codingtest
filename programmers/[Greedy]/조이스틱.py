# 조이스틱

def solution(name): 
    answer, idx = 0, 0
    asc = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    
    while True:
        answer += asc[idx]
        asc[idx] = 0
        
        if sum(asc) == 0:
            return answer
        
        left, right = 1, 1
        while asc[idx-left] == 0:
            left += 1
        while asc[idx+right] == 0:
            right += 1
            
        answer += left if left < right else right
        idx += -left if left < right else right
         
    return answer