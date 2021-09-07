import heapq

def solution(jobs):
    answer, now, n = 0, 0, 0
    start = -1
    heap = []
    
    while n < len(jobs):
        for request, process in jobs:
            # 현재 작업이 시작하고 끝날때까지 그 사이에 시작가능한 작업이 있다면 추가
            if start < request <= now:
                heapq.heappush(heap, [process,request] )
        # 작업이 있다면
        if len(heap) > 0:
            # 처리 시간이 가장 짧은 애를 투입
            curPro, curReq = heapq.heappop(heap)
            # 시작시간은 이전 작업의 종료시간으로 변경
            start = now
            # 새로운 종료시간은 (현재 종료시간 + 추가할 작업의 처리시간)
            now += curPro
            # 총 걸린 시간은 (최종 종료시간 - 요청 시작 시간)
            answer += (now-curReq)
            # 요청 하나 처리 완료
            n += 1
        else:
        # 작업이 없다면 범위 늘리기
            now += 1 
            
    return int(answer / len(jobs))