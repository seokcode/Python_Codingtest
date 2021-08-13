# 짝지어 제거하기

def solution(s):
    arr = []
    
    for item in s:
        if arr:
            if arr[-1] == item:
                arr.pop()
            else:
                arr.append(item)
        else:
            arr.append(item)
        
    return 1 if not arr else 0