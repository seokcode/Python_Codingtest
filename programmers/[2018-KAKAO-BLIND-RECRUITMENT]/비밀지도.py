# 비밀지도

def solution(n, arr1, arr2):
    ary = []
    ary2 = []
    ans = [['#'] * n for _ in range(n)]

    for i in arr1:
        ary.append((['0'] * (n - len(format(i,'b'))) + list(format(i,'b'))))

    for i in arr2:
        ary2.append((['0'] * (n - len(format(i,'b'))) + list(format(i,'b'))))

    for i in range(n):
        for j in range(n):
            if ary[i][j] == ary2[i][j] and ary[i][j] == '0':
                ans[i][j] = ' '
        ans[i] = ''.join(ans[i])

    return ans
