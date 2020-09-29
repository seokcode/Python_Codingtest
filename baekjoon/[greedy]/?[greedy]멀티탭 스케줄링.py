# 멀티탭 스케줄링 # B_1700
n, k = map(int, input().split())
s = list(map(int, input().split()))
m = [0 for i in range(n)]
cnt = 0
for i in range(k):
    isTrue = False
    for j in range(n):
        if m[j] == s[i] or m[j] == 0:
            isTrue = True
            m[j] = s[i]
            break
    if isTrue:
        continue
    else:
        a = 0
        for j in range(n):
            # s[i+1:] => i+1인덱스부터 끝까지 중에
            # index(m[j]) => m[j]가 몇번째 인덱스에 있는지
            if a < s[i+1:].index(m[j]):
                a = s[i+1:].index(m[j])
                b = j
        m[b] = s[i]
        cnt += 1
print(cnt)
