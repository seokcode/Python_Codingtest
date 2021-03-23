# 키패드 누르기

def solution(numbers, hand):
    answer = []
    left = 10
    right = 12
    for i in numbers:
        left_status = 0
        right_status = 0

        if i == 0:
            i = 11
        if i == 1 or i == 4 or i == 7:
            answer.append('L')
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer.append('R')
            right = i
        else:
            dl = (abs(left - i) // 3) + (abs(left - i) % 3)
            dr = (abs(right - i) // 3) + (abs(right - i) % 3)

            if dl > dr:
                answer.append('R')
                right = i
            elif dl == dr:
                if hand == "right":
                    answer.append('R')
                    right = i
                else:
                    answer.append('L')
                    left = i
            else:
                answer.append('L')
                left = i

    answer = ''.join(answer)
    return answer