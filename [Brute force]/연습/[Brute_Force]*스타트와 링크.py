# 스타트와 링크 # B_14889
# N제한(4<=N<=20)
# N명중에 N/2명을 골라서 두 팀으로 나누는 경우의수: N C N/2 -> 20 C 10
# 경우의 수 백만개 이하

"""
1. 백트래킹으로 푸는 방법 (백트래킹: 재귀함수를 이용한 브루트포스 방법.)
* 요구하는 답을 도출할 수 없을 때 불필요한 경우의 수를 만들지 않음으로써(재귀호출중단)
처리속도를 월등히 빨라지게
"""
def go(index, first, second):
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff

    # 백트래킹 컷팅조건: 팀이 n/2을 넘어서면 더 이상 구할 필요가 없음
    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1

    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
print(go(0, [], []))

"""
2. 비트마스크 풀이
n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
ans = -1
for i in range((1<<n)):
    cnt = 0
    for j in range(n):
        if (i&(1<<j)) > 0:
            cnt += 1
    if cnt != n//2:
        continue
    first = []
    second = []
    for j in range(n):
        if (i&(1<<j)) > 0:
            first += [j]
        else:
            second += [j]
    if len(first) != n//2:
        continue
    t1 = 0
    t2 = 0
    for l1 in range(n//2):
        for l2 in range(n//2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]
    diff = abs(t1-t2)
    if ans == -1 or ans > diff:
        ans = diff
print(ans)
"""
"""
3. 브루트 포스로 푸는 방법

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [0 if i < n/2 else 1 for i in range(n)]
ans = 100000000
while True:
    first = []
    second = []
    for i in range(n):
        if b[i] == 0:
            first.append(i)
        else:
            second.append(i)
    one = 0
    two = 0
    for i in range(n//2):
        for j in range(n//2):
            if i == j:
                continue
            one += a[first[i]][first[j]]
            two += a[second[i]][second[j]]
    diff = abs(one-two)
    if ans > diff:
        ans = diff
    if not next_permutation(b):
        break
print(ans)
"""