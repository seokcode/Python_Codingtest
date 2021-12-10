from collections import deque

def strToint(time):
    hour, minute = map(int, time.split(":"))
    return hour*60 + minute

def intTostr(time):
    hour = time // 60
    minute = time - (hour*60)
    
    return format(hour, '02')+":"+format(minute, '02')

def solution(n, t, m, timetable):
    shuttle = [540+(t * i) for i in range(n)]
    ride = [[0,0] for _ in range(len(shuttle))]
    timetable.sort()
    passengers = deque(timetable)
    
    idx = 0
    while passengers and idx < len(shuttle):
        if strToint(passengers[0]) <= shuttle[idx] and ride[idx][0] < m:
            ride[idx][0] += 1
            ride[idx][1] = strToint(passengers.popleft())
        else:
            idx += 1
    
    
    if ride[-1][0] == m:
        return intTostr(ride[-1][1]-1)
    else:    
        return intTostr(shuttle[-1])