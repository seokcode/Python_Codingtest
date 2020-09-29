# 프린터 큐 # B_1966
num = int(input())
for i in range(num):
    N, M = map(int, input().split())
    pr = list(map(int, input().split()))
    pr_ = [0 for i in range(N)]
    pr_[M] = 1
    count = 0
    while True:
        if pr[0] == max(pr):
            count += 1
            if pr_[0] == 1:
                print(count)
                break
            else:
                del pr[0]
                del pr_[0]

        else:
            pr.append(pr[0])
            del pr[0]
            pr_.append(pr_[0])
            del pr_[0]