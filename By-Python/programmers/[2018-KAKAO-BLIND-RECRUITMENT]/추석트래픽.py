def toMiliSec(string):
    h, m, s = map(float, string.split(":"))
    return int((h * 3600 + m * 60 + s)*1000)


# 입력받은 start로부터 1초라는 범위 내에 속한 log가 몇개인지 count
def countTraffic(start, logs):
    traffic = 0
    end = start+1000
    
    
    for log in logs:
        # log[0] = 시작시간, log[1] = 끝시간
        # log가 범위내에 속해있으려면 시작시간이 end 미만이어야하고 끝시간이 start 이상이어야한다
        # 걸쳐있는경우도 있기 때문
        if log[1] >= start and end > log[0]:
            traffic += 1
    
    return traffic

def solution(lines):
    answer = 1 # 트래픽은 최소 1개
    logs = []
    
    for l in lines:
        day, end, processTime = l.split(" ")
        
        end = toMiliSec(end) # 종료시간
        processTime = int(float(processTime[:-1])*1000) # 트래픽 처리 시간
        start = end-processTime+1 # 시작시간 = 종료시간-트래픽처리시간+0.001초
        
        # lines배열이 시간순으로 들어있기 때문에 시간이 빠른 순서대로 저장됨
        logs.append([start,end])
        
    # 시간이 빠른 순서대로 최대처리트래픽 도출시키기    
    for start,end in logs:
        answer = max(answer, countTraffic(start,logs), countTraffic(end,logs))
            
    return answer