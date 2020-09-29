# 자와 각도기 # B_2916
n, k = map(int, input().split())  # (알고 있는 각도/만들 수 있는지 알고 싶은 각도)의 수
c = list(map(int, input().split()))  # 아는 각도
h = list(map(int, input().split()))  # 만들 수 있는지 알고 싶은 각도
d = [False]*360  # d[i] = 각도 i를 만들 수 있는지
d[0] = True

for i in range(n):
    for q in range(360):
        for j in range(360):
            if not d[j]:  # j도가 만들 수 없는 각도면 패스
                continue

            # 만들 수 있는 각도면 이미 아는 각도를 더하고 뺀 각도도 만들 수 있는
            d[(j-c[i]+360) % 360] = True
            d[(j+c[i]) % 360] = True

for ans in h:
    if d[ans]:
        print('YES')
    else:
        print('NO')