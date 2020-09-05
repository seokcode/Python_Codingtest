# 회의실 배정 # B_1931
import sys
input = sys.stdin.readline

num = int(input())
meeting = []
for i in range(num):
    st, et = map(int, input().split())
    meeting.append((st, et))

# 시작 시간 순으로 오름차순 정렬
# 끝나는 시간으로 오름차순 정렬후
# --> 끝나는 시간이 빠르고, 끝나는 시간이 같을 경우
#     시작시간이 빠른 순으로 정렬
meeting = sorted(meeting, key=lambda time: [time[1], time[0]])

result = 0
before_finish_time = 0
for i in meeting:
    # 전 강의 끝난 시간보다 새 강의 시작시간이 느리면 가능
    # result ++
    if i[0] >= before_finish_time:
        before_finish_time = i[1]
        result += 1

print(result)
