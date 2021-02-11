# 4연산 # B_14395
"""
모두 연산의 비용 1
만들어지는 수는 항상 x->x^2 또는 2*x의 형태로 변형 가능
"""

from collections import deque
limit = 1000000000  # 수 제한 10^9
s, t = map(int,input().split())
check = set()
q = deque()
q.append((s,''))
check.add(s)

while q:
    x, s = q.popleft()
    if x == t:  # 정답을 찾은 경우
        if len(s) == 0:  # 수가 애초에 같아서 연산이 필요 없었다면
            s = '0'  # 0출력
        print(s)  # 정답(연산순서) 출력
        exit()

    # 가능한 연산 BFS로 다 해보기
    # 해당 연산 후의 수가 범위 내이고 아직 나오지 않은 수라면 실행
    if 0 <= x*x <= limit and x*x not in check:
        q.append((x*x, s+'*'))
        check.add(x*x)
    if 0 <= x+x <= limit and x+x not in check:
        q.append((x+x, s+'+'))
        check.add(x*x)
    if 0 <= x-x <= limit and x-x not in check:
        q.append((x-x, s+'-'))
        check.add(x*x)
    if x != 0 and 0 <= x//x <= limit and x//x not in check:
        q.append((x//x, s+'/'))
        check.add(x//x)
print(-1)
