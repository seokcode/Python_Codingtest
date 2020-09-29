# 브루트 포스란? 가능한 모든 경우의 수를 전부 다 해보는 거
# 이 때, 경우의 수를 다 해보는데 걸리는 시간이 문제의 시간 제한을 넘지 않아야 한다.
# 경우의 수가 백만, 천만 이하면 가능하다고 판단
# 브루트 포스 시간 복잡도는 O(경우의 수  * 방법 1개를 시도하는데 걸리는 시간)

# 일곱 난쟁이 # B_2309
# 아홉 명 중에 일곱 명을 고르는 것은 아홉 명 중에 두 명을 고르는 것과 같다.
# NC2(N개 중에 2개를 고르는 방법) = N(N-1)/2
# O(N^2)[방법의 수] * O(N)[값] = O(N^3)
import sys

num = 9
nan = [int(input()) for _ in range(num)]
nan.sort()
total = sum(nan)

for i in range(num):
    for j in range(i+1, num):
        if total - nan[i] - nan[j] == 100:
            for k in range(num):
                if i == k or j == k:
                    continue
                print(nan[k])
            sys.exit()


