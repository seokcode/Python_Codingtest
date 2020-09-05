# 주사위 # B_1041
# 계산 공식은 맞으나 3면이 보이는 경우에는
# 주사위의 면에 따른 최솟값이기 때문에 오름차순 정렬로 값 산정불가
# A B C D E F
# 0 1 2 3 4 5
# i+j ==5 -> 반대편
# 한 변은 가장 작은 값 선정
# 두 변은 i+j != 5(반대편 값이 아닌) 두 변의 합의 최솟값
# 세 변은 i+j != 5(반대편 값이 아닌) 세 변의 합의 최솟값

N = int(input())
s = list(map(int, input().split()))
result = 0
temp = [0] * 3

# [0]: 한 변 / [1]: 두 변이 필요한 / [2]: 세 변이 필요한
temp[0] = min(s)

temp[1] = 10000
for i in range(6):
    for j in range(i+1, 6):
        if i+j != 5:
            if s[i]+s[j] < temp[1]:
                temp[1] = s[i]+s[j]

temp[2] = sum(s)
for i in [0, 5]:
    for j in [1, 4]:
        for k in [2, 3]:
            temp[2] = min(temp[2], s[i]+s[j]+s[k])

if N == 1:
    print(sum(s)-max(s))
else:
    # 밑면
    base_side = 0
    # 밑면 꼭지점
    base_side += temp[1] * 4
    # 밑면 변
    base_side += temp[0] * 4 * (N - 2)
    # 윗면
    upper_side = 0
    # 윗면 꼭지점
    upper_side += temp[2] * 4
    # 윗면 변
    upper_side += temp[1] * 4 * (N - 2)
    # 윗면 중앙면
    upper_side += temp[0] * ((N - 2) ** 2)
    # 옆면
    side = 0
    # 옆면 꼭지점
    side += temp[1] * 4 * (N - 2)
    # 옆면 중앙면
    side += temp[0] * 4 * ((N - 2) ** 2)

    print(upper_side + side + base_side)
