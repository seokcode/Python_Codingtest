# 단어변환

def solution(begin, target, words):
    new_begin = [begin]
    ans = 0

    if target not in words:
        return 0

    while (len(words) != 0):
        for b in new_begin:
            possible = []
            for word in words:
                cnt = 0
                for j in range(len(b)):
                    if b[j] != word[j]:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 1:
                    possible.append(word)
                    words.remove(word)
        ans += 1
        if target in possible:
            return ans
        else:
            new_begin = possible

    return 0