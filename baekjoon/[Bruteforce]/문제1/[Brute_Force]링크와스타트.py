# 링크와 스타트 # B_15661
"""
# 스타트와 링크 문제는 사람 수가 항상 짝수
한 사람이 1팀 혹은 2팀으로 가는 선택지가 있음
n명일 경우 2^n 가지 => 2^20가지가 최대 1048576가지
"""


def go(index, first, second):
    if index == n:  # 답을 찾은 경우
        if len(first) == 0:  # 조건위반: 한 팀의 인원은 최소 1명 이상
            return -1
        if len(second) == 0:
            return -1
        t1 = 0
        t2 = 0
        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue
                t1 += s[p1][p2]  # 1팀의 능력치 합산
        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]  # 2팀의 능력치 합산
        diff = abs(t1-t2)
        return diff

    ans = -1
    t1 = go(index+1,first+[index],second)  # index번째 사람이 1팀에 들어가는 경우
    if ans == -1 or (t1 != -1 and ans > t1):  # diff의 최솟값
        ans = t1
    t2 = go(index + 1, first, second+[index])  # index번째 사람이 2팀에 들어가는 경우
    if ans == -1 or (t2 != -1 and ans > t2):  # diff의 최솟값
        ans = t2
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))
