# 병든 나이트 # B_1783
# 헷갈
N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M+1)//2))
else:
    if M <= 6:
        print(min(4, M))
    else:
        print(M - 2)