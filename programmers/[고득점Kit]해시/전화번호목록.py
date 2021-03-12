# 전화번호 목록

# 틀린코드 정확성+효율성 91.7/100.0
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                return answer

    return answer