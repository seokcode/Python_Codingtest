# 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0  # 답
    bridge = deque(0 for _ in range(bridge_length))  # 다리
    trucks = deque(truck_weights)  # 대기중인 트럭
    bridge_weight = 0  # 현재 다리의 무게

    # 다리를 다 건넜다면 bridge배열은 비어있게 된다
    while bridge:
        # 대기중인 트럭이 있다면
        if trucks:
            # 1초마다
            answer += 1
            # 다리의 끝에 있는 놈 탈출
            out = bridge.pop()
            # 탈출 한 놈 무게만큼 전체 다리의 무게에서 뺴주기
            bridge_weight -= out

            # 나올 차례인 트럭이 현재 다리에 올라가도 제한 무게 이하라면 올림
            if bridge_weight + trucks[0] <= weight:
                now = trucks.popleft()
                bridge_weight += now  # 트럭 무게만큼 현재 다리무게에 +
                bridge.appendleft(now)
            else:
                # 못올라가면 현재 다리 위 트럭들을 1칸씩 전진 시킴
                bridge.appendleft(0)
        else:
            # 대기중인 트럭이 없다면 트럭이 다 탈출할때까지 초 세기
            # 대기중인 트럭이 없다는 것은 가장 마지막 차례인 트럭이 올라갔다는 의미이므로 bridge배열의 0번 인덱스가 마지막 트럭의 위치
            bridge.pop()
            answer += 1

    return answer