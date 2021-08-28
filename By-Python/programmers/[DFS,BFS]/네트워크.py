# 네트워크

def solution(n, computers):
    check = [False for _ in range(n)]
    ans = 0

    def go(num):
        check[num] = True
        for idx,i in enumerate(computers[num]):
            if i == 1:
                if not check[idx]:
                    go(idx)

    for i in range(n):
        if not check[i]:
            go(i)
            ans +=1

    return ans