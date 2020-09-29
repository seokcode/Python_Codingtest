"""
# 비트마스크
# 비트 연산을 사용해서 부분 집합을 표현할 수 있다.
# 비트 연산: &(and), |(or), ~(not), ^(xor)
## or연산은 둘 중 하나만 1이어도 1 /  (1, 1)도 1
## xor연산은 둘 중 하나만 1이어야 1 / (1, 1)은 0
# 여기서 not 연산은 자료형에 따라 결과가 달라진다.

# 8비트 자료형의 경우 A=1010011 7자리라면 01010011으로 가정하여 ~A=10101100
# 또한 signed 자료형 일때는 ~A=-84이지만 unsigned자료형이라면 ~A의 이진수계산
# 1 << 0 = 1  1 << 1 = 2(10의 이진수) 1 << 2 = 4(100의 이진수)
# A<<B는 A*2^B와 같고 A>>B는 A/2^B와 같음

# 비트 마스크 : 꼭 0 부터 N-1까지 정수로 이루어진 집합을 나타낼때 사용한다.
# {1,3,4,5,9} = 570 = 1000111010 = 2^1 + 2^3 + 2^4 + 2^5 + 2^9
# 값이 있는지 확인: S & (1<<i) # 값을 추가: S | (1<<i)
# 값을 제거: 570 & -2^1 = S & ~(1<<i) # 토글: 1->0 0->1 : S ^ (1<<i)

# 1 << N - 1은 (1 << N) - 1일까? 1 << (N - 1)일까?
# 정답은 1 << (N - 1)
"""
# 집합 # B_11723
# pypy3 시간초과 python3로 돌리기
import sys
n = 20
m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    op, *num = sys.stdin.readline().split()
    if len(num) > 0:
        # 비트마스크는 0~N-1의 수를 사용해야하기 때문
         x = int(num[0])-1
         print(x)
    if op == 'add':
        s = (s | (1 << x))
    elif op == 'remove':
        s = (s & ~(1 << x))
    elif op == 'check':
        res = (s & (1 << x))
        if res > 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle':
        s = (s ^ (1 << x))
    elif op == 'all':
        s = (1 << n) - 1
    else:
        s = 0