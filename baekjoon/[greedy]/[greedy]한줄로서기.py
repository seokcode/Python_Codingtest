# 한 줄로 서기 # B_1138
import sys
input = sys.stdin.readline

# 사람 수
n = int(input())
# 자신의 왼쪽에 있는 자신보다 큰 사람 수
order = list(map(int, input().split()))
# 사람 수 길이 만큼 리스트 선언(사람 수 만큼 줄 세움)
sol = [0 for i in range(n)]
for i in range(1, n+1):
    # count는 order[i-1]과 동일해야함
    count = 0
    # 한 명씩 줄 세우기
    temp = order[i-1]
    for j in range(n):
        # 현 위치가 비었고 왼쪽에 temp 만큼의 공간이 있으면 위치시킴
        if count == temp and sol[j] == 0:
            sol[j] = i
            # 그리고 빠져나감
            break
        # 위 if문을 만족하지 않는다면 count 증가
        if sol[j] == 0:
            count += 1
for a in sol:
    print(a, end=' ')
# == print(*sol)
