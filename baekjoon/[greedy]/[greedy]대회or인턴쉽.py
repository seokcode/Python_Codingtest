# 대회 or 인턴쉽 # B_2875
import sys
input = sys.stdin.readline

male, female, internship = map(int, input().split())

t_m = male // 2
result = 0
if t_m >= female:
    # 여자는 다 참여, 참여하고 남은 남자가 인턴쉽에 갈 수 있으면
    result = female
    while (male - 2 * result) + (female - result) < internship:
        result -= 1

else:
    result = t_m
    # 남자는 다 참여
    # 인턴쉽에 갈 사람이 부족한 동안 반복
    # 참여하고 남은 남+여
    while (male - 2 * result) + (female - result) < internship:
        result -= 1

print(result)
