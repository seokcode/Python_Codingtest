# 부분집합의 합 # B_1182
# 재귀 함수
# 2^n가지의 경우의 수

n, goal = map(int, input().split())
a = list(map(int, input().split()))
ans = 0


def select(i, s):
    # 2,-2,2 중에 합이 2인 것을 구할경우 2와 2,-2,2 둘 다 답이 되기
    # 때문에 자릿수별로 모두 구해야 함 그렇지 않다면 2만 구하고 넘어가버림
    global ans
    if i == n:
        if s == goal:  # 정답을 찾음
            ans += 1
        return

    select(i + 1, s + a[i])  # 포함한다
    select(i + 1, s)  # 포함하지 않는다


select(0, 0)
# 문제에서 공집합은 제외하라고 함
# 합이 0을 구하는 방법 중 아무것도 선택하지 않는 것이 포함되어 있기 때문에
# 1개를 빼줘야 함
if goal == 0:
    ans -= 1
print(ans)
