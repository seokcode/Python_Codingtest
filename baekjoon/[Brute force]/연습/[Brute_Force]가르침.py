# 가르침 # B_1062
# 비트마스크
def count(mask, words):
    cnt = 0
    for word in words:
        # mask: 배운 알파벳, ~mask: 안배운 알파벳
        # word에서 1인것?: 단어에 포함되어 있는 알파벳
        # (1<<26)-1-mask)에서 1인것? : 내가 안배운 알파벳
        # 두개를 &연산해서 0이 나왔다면 안배운 그 단어에 모르는 알파벳이 없다는 것
        if (word & ((1<<26)-1-mask)) == 0:
            cnt += 1
    return cnt

# mask:배운 알파벳, k=m(배울 수 있는 알파벳 수)
def go(index, k, mask, words):
    if k < 0:
        return 0
    if index == 26:  # 알파벳의 토탈 갯수=26
        return count(mask, words)
    ans = 0
    # 단어를 배웠으면 mask | (1<<index)로 추가해주고
    t1 = go(index+1, k-1, mask | (1<<index), words)
    if ans < t1:
        ans = t1
    if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
        # 안배웠으면 그냥 mask만 보냄
        t2 = go(index+1, k, mask, words)
        if ans < t2:
            ans = t2
    return ans

n,m = map(int,input().split())
words = [0] * n
for i in range(n):
    s = input()
    for x in s:
        # 입력된 각 알파벳의 ascii 코드 값 & a의 ascii 코드 값의 차이를 기준
        words[i] |= (1 << (ord(x)-ord('a')))
print(go(0,m,0,words))