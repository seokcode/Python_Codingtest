"""
# 다이나믹 프로그래밍: 큰 문제를 작은 문제로 나눠서 푸는 알고리즘
# 분할 정복은 작은 문제들이 중복되지 않지만 DP는 작은 문제들이 중복된다는 점에서 다름
# 피보나치 수열: F(n) = F(n-1) + F(n-2) (n>=2) 이 대표적인 DP
# DP 알고리즘을 적용시키기 위한 조건

1. Overlapping Subproblem: 작은 문제들이 중복되어 큰 문제를 이룸
2. Optimal Substructure: 문제의 정답을 작은 문제의 정답에서 구할 수 있다.

DP에서 각 문제는 한 번만 풀어야 한다.
Optimal Substructure를 만족하기 때문에, 같은 문제는 구할 때마다 정답이 같다.
따라서, 정답을 한 번 구했으면, 정답을 어딘가에 메모해놓는다. ## DP의 핵심
(배열 사용 == Momoization)
"""

# DP Memoization을 이용한 피보나치 수
# 시간복잡도: 모든 문제는 1번씩만 푼다(즉, 답을 구하는데에는 n번걸림) * 함수의 시간복잡도(1)
# 즉, 총 시간 복잡도: O(n)
memo = [0]*100

def fibonacci(n):
    if n <= 1:
        return n
    else:
        if memo[n] > 0:
            return memo[n]
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

"""
# 재귀함수를 이용한 피보나치 수(Top-down)
# 시간 복잡도:  O(2n^2)
d= [0]*100
def fibonacci(n):
    if n <= 1:
        return n
    else:
        d[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

# for 문을 이용한 피보나치 수(Bottom-up)
memo = [0]*100
def fibonacci(n):
    d[0] = 0
    d[1] = 1
    for i in range(2,n+1):
        d[i] = d[i-1] + d[i-2]
        
    return d[n]
"""
