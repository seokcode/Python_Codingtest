# 1,2,3 더하기 # B_9095
# N중 for문
# n <= 10 이므로 나올 수 있는 항의 갯수는 최대 10개(1+1+1+...)
# 수는 1, 2, 3이므로 3^10은 < 10 만이므로 브루트 포스 알고리즘 적용
# 시간 복잡도 = O(3^n)

tc = int(input())

for i in range(tc):
    ans = 0
    n = int(input())
    for l1 in range(1, 4):
        if l1 == n:
            ans += 1
        for l2 in range(1, 4):
            if l1 + l2 == n:
                ans += 1
            for l3 in range(1, 4):
                if l1 + l2 + l3 == n:
                    ans += 1
                for l4 in range(1, 4):
                    if l1 + l2 + l3 + l4 == n:
                        ans += 1
                    for l5 in range(1, 4):
                        if l1 + l2 + l3 + l4 + l5 == n:
                            ans += 1
                        for l6 in range(1, 4):
                            if l1 + l2 + l3 + l4 + l5 + l6 == n:
                                ans += 1
                            for l7 in range(1, 4):
                                if l1 + l2 + l3 + l4 + l5 + l6 + l7 == n:
                                    ans += 1
                                for l8 in range(1, 4):
                                    if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == n:
                                        ans += 1
                                    for l9 in range(1, 4):
                                        if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 == n:
                                            ans += 1
                                        for l10 in range(1, 4):
                                            if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 == n:
                                                ans += 1

    print(ans)