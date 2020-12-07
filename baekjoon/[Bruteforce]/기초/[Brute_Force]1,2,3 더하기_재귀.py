# 1,2,3더하기 # B_9095
# 재귀함수
# 1. 불가능한 경우: 정답을 찾을 수 없는 경우(sum > goal)
# 2. 정답을 찾은 경우
# 3. 아직 답을 찾지 못한 경우: 다음 경우를 호출
#    3-1. 1을 사용 : go(count + 1, sum + 1, goal)
#    3-2. 2를 사용 : go(count + 1, sum + 2, goal)
#    3-3. 3을 사용 : go(count + 1, sum + 3, goal)
# 시간 복잡도 O(3^n)


def go(s, goal):
    if s > goal:
        # 불가능한 경우
        print('no!')
        return 0
    if s == goal:
        # 정답을 찾은 경우
        print('find!')
        return 1
    now = 0
    # 숫자 1,2,3 사용
    for i in range(1, 4):
        now += go(s + i, goal)
        print(now)
    return now


N = int(input())
for _ in range(N):
    goal = int(input())
    print(go(0, goal))
