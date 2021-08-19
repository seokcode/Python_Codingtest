from collections import defaultdict

# 통과 # len(set(cart))대신 dictionary사용
def solution(gems):
    if len(gems) == 1: return [1]
    
    gemNum = len(set(gems))
    cart = defaultdict(list)
    answer = [1,len(gems)]
    start = 0
    
    for end in range(len(gems)):
        cart[gems[end]] = cart.get(gems[end], 0) + 1
        
        while (len(cart) == gemNum) and (start <= end):
            if (answer[1]-answer[0]) > (end-start):
                answer = [start+1, end+1]
            
            cart[gems[start]] -= 1
            
            if cart[gems[start]] == 0:
                del cart[gems[start]]
            
            start += 1
                
    return answer