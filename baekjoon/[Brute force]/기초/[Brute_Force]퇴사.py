# 퇴사 # B_14501
# 1. 불가능한 경우: day > n+1
# 2. 정답: day == n+1(n+1일에는 상담 여부를 결정할 필요 없음)
# 3. 다음 경우: 상담을 함 -> 상담 날짜만큼 이동 / 하지 않음
# 첫날: 1 마지막:n 퇴사:n+1
# 문제에서는 인덱스가 0부터 시작하므로 첫날: 0 마지막: n-1 퇴사: n

n = int(input())
T = [0] * n  # 상담에 걸리는 시간
P = [0] * n  # 해당 상담으로 버는 돈

for i in range(n):
    T[i], P[i] = map(int, input().split())

ans = 0  # 답이 될 변수


# day일이 되었다. day일에 있는 상담을 할지 말지 결정해야 한다. %= index
# 지금까지 얻은 수입은 s이다.
def retire(day, s):
    global ans
    if day == n:  # 2. 정답(날짜가 퇴사 날짜가 되었을 때)
        ans = max(ans, s)
        return
    if day > n: # 3. 불가능(날짜가 퇴사 날짜를 지났을 때)
        return
    retire(day + T[day], s + P[day])
    retire(day + 1, s)


retire(0, 0)
print(ans)
