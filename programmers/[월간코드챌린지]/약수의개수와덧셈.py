# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0   
    
    for number in range(left,right+1):
        divisor = set()
        divisor.add(1)
        for j in range(1, (number//2)+1):
            if number % j == 0:
                divisor.add(j)
                if j != (number // j):
                    divisor.add(number//j)  
        if len(divisor) % 2 == 0:
            answer += number
        else:
            answer -= number
            
    return answer