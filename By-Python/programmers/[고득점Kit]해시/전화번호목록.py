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

# 정답
# for문이 두개일 필요가 없음
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True

# 해시를 이용한 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer