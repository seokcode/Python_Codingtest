# LCD Test # B_2290
"""
    0123
0번그룹    00
1번그룹   1  2
1번그룹   1  2
2번그룹    33
3번그룹   4  5
3번그룹   4  5
4번그룹    66

"""
import sys
print = sys.stdout.write
c = (
    (1,1,1,0,1,1,1),  # 0의 모양을 나타냄
    (0,0,1,0,0,1,0),  # 1
    (1,0,1,1,1,0,1),  # 2
    (1,0,1,1,0,1,1),  # 3
    (0,1,1,1,0,1,0),  # ...
    (1,1,0,1,0,1,1),
    (1,1,0,1,1,1,1),
    (1,0,1,0,0,1,0),
    (1,1,1,1,1,1,1),
    (1,1,1,1,0,1,1)
)
s,n = input().split()
s = int(s)
m = len(n)
for i in range(5):  # 그룹 갯수만큼 반복
    if i in [0,2,4]:  # 0,2,4 그룹은 '-'를 출력
        for j in range(m):
            now = int(n[j])
            # 숫자 사이에는 한칸의 공백이 있어야 함
            if j != 0:
                print (' ')
            print(' ')
            if (i == 0 and c[now][0]) or (i == 2 and c[now][3]) or (i == 4 and c[now][6]):
                print('-'*s)
            else:
                print(' '*s)
            print(' ')
        print('\n')
    else:  # 그 외에는 '|'를 출력
        for l in range(s):
            for j in range(m):
                now = int(n[j])
                if j != 0:
                    print(' ')
                if (i == 1 and c[now][1]) or (i == 3 and c[now][4]):
                    print('|')
                else:
                    print (' ')
                print(' '*s)
                if (i == 1 and c[now][2]) or (i == 3 and c[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')

