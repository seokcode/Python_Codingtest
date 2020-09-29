# 부분집합의 합 # B_1182
# 비트마스크 # 시간복잡도: O(N*2^N)

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(1, (1 << n)):
    s = sum(a[k] for k in range(n) if (i & (1 << k)) > 0)
    if m == s:
        ans += 1
print(ans)
