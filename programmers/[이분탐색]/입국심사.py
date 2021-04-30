# 입국 심사

def solution(n, times):
    times.sort()
    answer, mintime = 0, 1
    maxtime = times[-1]*n
    
    while mintime <= maxtime:
        avg = (maxtime+mintime)//2
        count = 0
        for i in times:
            count += avg // i
            
            if count >= n:
                break
                
        if count >= n:
            answer = avg
            maxtime = avg - 1
        else:
            mintime = avg + 1

    return answer