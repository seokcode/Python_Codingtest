# DNA # B_1969

N, M = map(int, input().split())
s = [0] * M  # 답 DNA 리스트
sen = []  # 보기를 담을 리스트
a = 0
cnt = 0
ACGT = ['A', 'C', 'G', 'T']  # 유전자 종류

# sen 배열에 보기 DNA 코드를 쭉 연결해서 담음
for i in range(N):
    temp = list(input())
    for j in range(M):
        sen.append(temp[j])

# a+M*j 라는 수식을 사용하여 sen에 담긴 코드를 각 코드 별 앞자리부터
# M 자리 까지 비교
# 카운트 하여 제일 많은 종류를 s(결과) 리스트에 담고 나머지 카운트를 합하여 차이 계산
for i in range(M):
    acgt = [0, 0, 0, 0]
    for j in range(N):
        if sen[a+M*j] == 'A':
            acgt[0] += 1
        elif sen[a+M*j] == 'C':
            acgt[1] += 1
        elif sen[a + M * j] == 'G':
            acgt[2] += 1
        elif sen[a + M * j] == 'T':
            acgt[3] += 1
    s[i] = ACGT[acgt.index(max(acgt))]
    cnt += acgt[0]+acgt[1]+acgt[2]+acgt[3] - max(acgt)
    a += 1

print(''.join(s))
print(cnt)
