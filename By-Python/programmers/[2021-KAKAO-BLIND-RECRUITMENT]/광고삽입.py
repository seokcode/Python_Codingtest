# 광고 삽입 
# 21' kakao blind - 72414

def strTosec(string):
    h, m, s = map(int, string.split(":"))
    return h * 3600 + m * 60 + s

def secTostr(s):
    h = s // 3600
    s -= h * 3600
    m = s // 60
    s -= m * 60
    
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}:{str(s).zfill(2)}"

        
def solution(play_time, adv_time, logs):
    
    play_time = strTosec(play_time)
    adv_time = strTosec(adv_time)
    
    timeline = [0] * (play_time+1)
    
    for l in logs:
        start, end = map(strTosec, l.split("-"))
        # 영상 시작 시점에는 시청자가 추가됨
        timeline[start] += 1
        # 영상 종료 시점에는 시청자가 빠짐
        timeline[end] -= 1
    
    for _ in range(2):
        # 처음 돌 때는 비어있는 시간대에 시청자 수 채우기
        # 두번째 돌 때는 해당 시간대에 누적 시청자 수 채우기
        for t in range(1, play_time+1):
            timeline[t] += timeline[t-1]
        
    answer =0
    
    # 0초부터 광고를 넣었을 때 시청자 수
    maxSee = timeline[adv_time]
    
    for start in range(1, play_time):
        # 광고 종료 시간이 영상 재생시간을 넘어가면 광고 재생 종료 시간을 영상 종료 시간(play_time)으로 둔다.
        end = play_time if start + adv_time >= play_time else start + adv_time 
        
        # 시청자 수가 이전 답보다 많을 때를 찾으면서 값을 업데이트
        if maxSee < timeline[end] - timeline[start]:
            maxSee = timeline[end] - timeline[start]
            answer = start + 1
            # 여기서 1초를 더해준 이유는 timeline[end] - timeline[start]가
            # start+1초 부터 end초사이의 누적 시간이기 때문에
            
    return secTostr(answer)