# A->B # B_16953

from collections import deque

a, b = map(int, input().split())
q = deque()
q.append((a, 1))
ans = -1

while q:
    a, cnt = q.popleft()

    if a == b:
        ans = cnt
        break

    if a * 2 <= b:
        q.append((a * 2, cnt + 1))
    if int(str(a) + '1') <= b:
        q.append((int(str(a) + '1'), cnt + 1))

print(ans)