# 신입사원 # B_1946
import sys
input = sys.stdin.readline
# test case 갯수
t_case = int(input())

for i in range(t_case):
    num = int(input())
    score = []
    # 첫번째 인덱스 카운트한 상태로 시작
    count = 1
    # 첫번째 인덱스 값을 보관하기위한 임시공간
    temp = 0
    # 전 값 비교를 위한 임시공
    before = 0

    # 첫번째 면접, 두번째 면접 점수 저
    for j in range(num):
        f, s = map(int, input().split())
        score.append((f, s))
    # 첫번째 면접 점수 오름차순 정렬
    score = sorted(score, key=lambda sc: sc[0])
    # 첫번째 인덱스의 두번째 면접 점수와 비교
    for k in score:
        if temp == 0:
            temp = k[1]
            before = k[1]
        else:
            # 첫 번째 면접은 오름차순이기 때문에
            # 전 사람의 두번째 면접 점수보다 작아야 카운트
            if temp > k[1] and k[1] < before:
                before = k[1]
                count += 1
    print(count)
