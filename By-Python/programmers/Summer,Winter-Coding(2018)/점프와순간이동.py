# 점프와 순간이동

# 정확성 100.0 효율성 0.0 총점 60.0
def solution(n):
    d = [i for i in range(n+1)]
    
    for i in range(2,n+1):
        if i%2 == 0 : 
            d[i] = d[i//2]
        else:
            d[i] = d[i-1]+1

    return d[n]

# 통과
def solution(n):
    answer = 0
    
    while n != 0:
        if n % 2 != 0:
            answer += 1
            n -= 1
        else:
            n /= 2
            
    return answer