# 0과1 # B_8111
# 342 = ((3*10)+4)*10)+2
# 어떤 수를 n으로 나눈 나머지는 항상 n보다 작다
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    via = [-1]*n
    how = [-1]*n
    dist = [-1]*n
    q = deque()
    q.append(1%n)
    dist[1%n] = 0
    how[1%n] = 1
    while q:
        now = q.popleft()
        for i in [0,1]:
            next = (now*10+i)%n
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                via[next] = now
                how[next] = i
                q.append(next)

    if dist[0] == -1:
        print('BRAK')
    else:
        ans = ''  # 답이 될 문자열
        i = 0
        while i != -1:
            ans += str(how[i])  # 정답을 역순으로 저장
            i = via[i]
        print(ans[::-1])  # 인덱스 처음부터 끝까지 -1칸 간격으로(역순으로 출력)
