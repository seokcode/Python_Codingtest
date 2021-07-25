def solution(s):
    answer, temp = "", ""
    numbers = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in s :
        if i.isdigit():
            answer += i
            continue
        temp += i
        if temp in numbers:
            answer += numbers[temp]
            temp = ""
        
    return int(answer)