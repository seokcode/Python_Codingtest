# 부등호 # B_2529
"""
# 부등호의 개수가 k개 일 때 부등호를 만족하는 수 중 최대 정수 수열은 0~9까지 중 내림차순
으로 k+1개를 고른 수에서 나오게 된다
# 최소는 그 반대
"""
# 1.백트래킹으로 푸는 방법(순열로 푸는 것 보다 더 효율적)
def good(x, y, op):  # 컷팅 조건: 부등호를 만족하지 않으면 그만 둠
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True
def go(index, num):
    if index == n+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]):
            check[i] = True  # 수를 사용함
            go(index+1, num+str(i))
            check[i] = False # 다시 미사용으로 돌려놓음

n = int(input())
a = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])

"""
2. 순열로 푸는 방법
def next_permutation(sm):
    i = len(sm)-1
    while i > 0 and sm[i-1] >= sm[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(sm)-1
    while sm[j] <= sm[i-1]:
        j -= 1

    sm[i-1],sm[j] = sm[j],sm[i-1]
    j = len(sm)-1

    while i < j:
        sm[i], sm[j] = sm[j], sm[i]
        i += 1
        j -= 1

    return True

def prev_permutation(big):
    i = len(big) - 1
    while i > 0 and big[i-1] <= big[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(big)-1
    while big[j] >= big[i-1]:
        j -= 1

    big[i-1], big[j] = big[j], big[i-1]

    j = len(big)-1
    while i<j:
        big[i], big[j] = big[j], big[i]
        i += 1
        j -= 1

    return True


def check(perm, a):
    # 아래 포문에서 하나도 안걸리면 모든 부등호 만족함, True 리턴
    for i in range(len(a)):
        if a[i] == '<' and perm[i] > perm[i+1]:
            return False
        if a[i] == '>' and perm[i] < perm[i+1]:
            return False
    return True


k = int(input())  # 부등호의 갯수
a = input().split() # 부등호 리스트
small = [i for i in range(k+1)]  # K=2이라면 0,1,2
big = [9-i for i in range(k+1)]  # 9,8,7

while True:
    if check(small,a):
        break
    if not next_permutation(small):
        break

while True:
    if check(big, a):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
"""