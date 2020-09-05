# 문자열 # B_1120
import sys

a, b = list(sys.stdin.readline().split())
result = []
# 문자열 a를 좌측 혹은 우측 정렬했을때 b와의 차이만큼 반복
# adaabc-  -adaabc
# aababbc  aababbc
# 0110010  0010100
for i in range(len(b)-len(a)+1):
    count = 0
    # 문자열 a의 길이만큼 문자열 b와 비교
    for j in range(len(a)):
        if a[j] != b[j+i]:
            count += 1
    # 차이를 result 라는 리스트에 저장
    result.append(count)

# 값 중 최솟값 출력
print(min(result))

