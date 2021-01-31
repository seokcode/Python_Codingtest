# 문자열 압축

def solution(s):
    n = len(list(s)) // 2
    result = []

    for i in range(1, n + 1):
        stack = []
        compressed = ""
        for j in range(0, len(list(s)), i):
            if len(stack) >= 1 and s[j:j + i] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([s[j:j + i], 1])

        compressed += ''.join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
        result.append(len(compressed))

    return min(result) if result else 1