# 괄호변환


# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
def devide(w):
    open_bracket = 0
    close_bracket = 0
    for i in range(len(w)):
        if w[i] == '(':
            open_bracket += 1
        else:
            close_bracket += 1
        # u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        if open_bracket == close_bracket:
            return w[:i + 1], w[i + 1:]


# u가 "올바른 괄호 문자열"인지 검사
def checking(u):
    temp = []
    for i in u:
        if i == '(':
            temp.append(i)
        else:
            if not temp:
                return False
            # temp가 비어있지 않다는 것은 '('이 들어있다는 것이고 현재 ')'이 나왔기에 else문에 들어온 것이므로
            # '()'이 완성되었으므로 효율을 위해 append 해주지 않고 '('를 pop 해줌
            temp.pop()
    return True


def solution(p):
    # 1
    if p == "":
        return ""

    # 2
    u, v = devide(p)

    # 3.문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if checking(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer