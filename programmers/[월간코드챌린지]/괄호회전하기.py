# 괄호 회전하기

from collections import deque

def rotate(arr):
    temp = arr.popleft()
    arr.append(temp)
    return arr

def check(arr,forCheck):
    stack = []
    for i in arr:
        if i in "[{(":
            stack.append(i)
        else:
            if stack:
                if forCheck[i] != stack.pop():
                    return False
            else:
                return False
    if not stack:
        return True
            
def solution(s):
    answer = 0
    d = deque(s)
    forCheck = {']':'[', '}':'{', ')':'('}
    
    for i in range(len(s)):
        d = rotate(d)
        if check(d, forCheck):
            answer += 1

    return answer