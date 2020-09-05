# 연산자 끼워넣기 # B_14888
# 수의 자리는 바뀌지 않음
# 수열 [1,2,3,4,5,6]에 연산자 +(2개) -(1개) *(1개) /(1개)인 경우
# 연산자가 위치할 경우의 수 : 5!/2! * 1! * 1! * 1! = 60
# +,-,*,/ 를 로또 문제처럼 숫자로 표기하여 풀이
# N의 갯수가 11개 이하 -> 연산자 갯수는 N-1개 필요하므로 10이하 => 가능


def soonyeol(sy):

    i = len(sy) - 1
    while i > 0 and sy[i-1] >= sy[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(sy) - 1
    while sy[j] <= sy[i-1]:
        j -= 1
    sy[i-1], sy[j] = sy[j], sy[i-1]  # swap

    j = len(sy) - 1
    while i < j:
        sy[i], sy[j] = sy[j], sy[i]  # swap
        i += 1
        j -= 1

    return True

# 나눗셈은 음수일 경우 제대로 시행이 되지 않기때문에
# 함수를 통해 예외처리를 해줘야함
def div(a,t):
    if a >= 0:
        return a//t
    else:
        return -(-a//t)


def calc(a, c):
    n = len(a)
    ans_c = a[0]
    for i in range(1, n):
        if c[i-1] == 0:
            ans_c = ans_c + a[i]
        elif c[i-1] == 1:
            ans_c = ans_c - a[i]
        elif c[i-1] == 2:
            ans_c = ans_c * a[i]
        else:
            ans_c = div(ans_c, a[i])
    return ans_c


N = int(input())
a = list(map(int, input().split()))  # 숫자 저장 # 숫자는 입력 그대로 연산 시행
b = list(map(int, input().split()))  # 연산자 저장
c = []  # 연산자를 숫자로 대치하여 저장

# + - * / 연산의 숫자가 b에 저장되어있음
# 포문을 돌리게 되면 2,0,1,1이 enumerate를통해서
# i: 0 cnt: 2 / i: 1 cnt: 0 / i:2 cnt:1 이런식으로 i = 0은 +를 지칭 1은 -를 지칭하게 됨
for i, cnt in enumerate(b):
    for k in range(cnt):  # 연산자 갯수만큼 c 리스트에 연산자 번호 append
        print(k)
        c.append(i)

c.sort()  # 첫 순열은 오름차순
ans = []
while True:
    temp = calc(a, c)
    ans.append(temp)
    if not soonyeol(c):
        break

print(max(ans))
print(min(ans))
