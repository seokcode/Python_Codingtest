# 잃어버린 괄호 # B_1541

# 식에서 -를 기준으로 나누어 문자열 저장
# 55-50+40 >> ['55', '50+40']
s = input().split('-')
# 최종적으로 더할 수를 저장할 리스트 선언
num = []
# 주어진 식을 '-'기준으로 나눈 배열의 요소들 중
# '+'를 기준으로 나누어 더한 후 num 리스트에 저장
# ['55'], ['50', '40'] >> num ['55', '90']
for i in s:
    cnt = 0
    a = i.split('+')
    for j in a:
        cnt += int(j)
    num.append(cnt)
# 식의 첫 값은 연산자로 시작할 수 없으므로 인덱스 1부터 시작
result = num[0]
for i in range(1, len(num)):
    result -= num[i]
    # 55 - 90 = -35
print(result)