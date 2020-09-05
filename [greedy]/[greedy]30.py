# 30 # B_10610
# 문자열 그대로 사용
num = input()
sum = 0

# 30의 배수일 조건
# 1. 10의 배수 >> 0이 있어야함
# 2. 각 자릿수의 합이 3의 배수
if '0' not in num:
    print(-1)
else:
    for i in num:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        # 내림차순으로 정렬하면 가장 큰 수가 됨
        num = sorted(num, reverse=True)
        # 각 인덱스에서 숫자를 뽑아 출력
        print("".join(num))
