# 한수 # B_1065

n = int(input())

# 두자리까진 모두 등차수열
if n < 100:
    ans = n
else:
    ans = 99
    for i in range(100, n+1):
        i = list(map(int, str(i)))
        # 1000은 등차가 아니므로 999까지를 계산하면 되기 때문에 0,1,2인덱스만 검사하면 됨
        if i[0] - i[1] == i[1] - i[2]:
            ans += 1

print(ans)
