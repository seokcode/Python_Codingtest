# iSharp # B_3568
# 교안참고(문제1)

s = input()
a = []
now = ''
for x in s:
    if x in ' ,;':  # x가 공백이나 , ; 이면 끊고 a배열에 추가
        if now:
            a.append(now)
        now = ''
    else:
        now += x
base = a[0]  # 첫번째는 항상 자료형의 기본 타입
for i in range(1, len(a)):
    t = base
    s = list(a[i])

    # 어떤 문자열의 뒤에서 알파벳이 아닌게 나오면 기본자료형 t에 이어 붙임
    while s and not('a' <= s[-1] <= 'z'):
        # ][ 이렇게 붙여지면 안되므로 대괄호의 경우 변환 필요
        if s[-1] == '[':
            t += ']'
        elif s[-1] == ']':
            t += '['
        else:
            t += s[-1]
        s.pop()
    print(t + ' ' + ''.join(s) + ';')

