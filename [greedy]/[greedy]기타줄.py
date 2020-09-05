# 기타줄 # B_1049
import sys
input = sys.stdin.readline

# N은 끊어진 줄 갯수, M은 줄 브랜드 갯수
N, M = map(int, input().split())

package = []
seperate = []
six_p = 0

# 브랜드 별로 6개 한묶음 가격과 낱개 가격 입력
for i in range(M):
    p, s = map(int, input().split())
    package.append(p)
    seperate.append(s)

# 만일 6개 패키지 가격 <= 낱개 * 6 가격 이라면
# 6개가 필요할 때 패키지 하나로 해결
if min(package) <= min(seperate)*6:
    six_p = min(package)
else:
    six_p = min(seperate)*6

# 끊어진 줄이 6개 이하일 경우
# 한 팩보다 낱개 * N의 가격이 높다면 한팩 구매
if N <= 6:
    if min(package) <= min(seperate)*N:
        print(min(package))
    else:
        print(min(seperate)*N)
# 끊어진 줄이 6개 초과일 경우
# pack: N을 6개로 나눈 몫 / temp: N을 6개로 나눈 나머지
# 한 팩보다 낱개*나머지 의 가격이 높을경우 한팩 + 한팩*몫 구매
# 아닐경우 낱개*나머지 + 한팩*몫 구매
else:
    pack = N // 6
    temp = N % 6
    if min(package) <= min(seperate)*temp:
        print(min(package)+six_p*pack)
    else:
        print(min(seperate)*temp+six_p*pack)