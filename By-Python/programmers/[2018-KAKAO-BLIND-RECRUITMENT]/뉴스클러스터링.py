# 뉴스 클러스터링

import re
def solution(str1, str2):
    # 영문으로만 2글자 이상인지 체크하기위한 정규식
    p = re.compile('[a-z]{2}')

    # 문자열을 두 글자씩 끊어 리스트로 만들어주는 메서드
    def split_list(string):
        leng = len(string)
        string = string.lower() # 전부 소문자로 변환
        i = 0 ; j = 1
        arr = []
        for _ in range(leng-1):
            res = string[i] + string[j]
            if p.match(res):
                arr.append(res)
            i += 1
            j += 1
        return arr

    list_A = split_list(str1) # str1
    list_B = split_list(str2) # str2

    set_A = set(list_A)
    set_B = set(list_B)
    types = set(set_A | set_B)  # 각 A, B 집합의 합집합의 모든 종류

    # 교집합, 합집합 종류를 count 해주는 dictionary
    inter_dic = {}
    union_dic = {}
    for t in types:
        a_count = list_A.count(t)
        b_count = list_B.count(t)
        inter_dic[t] = min(a_count, b_count)
        union_dic[t] = max(a_count, b_count)

    # 다중 집합의 교집합
    intersection = []
    for key in inter_dic:
        # 교집합에 포함된 갯수만큼 append
        for i in range(inter_dic[key]):
            intersection.append(key)

    # 다중 집합의 합집합
    union = []
    for key in union_dic:
        # 합집합에 포함된 갯수만큼 append
        for i in range(union_dic[key]):
            union.append(key)

    answer = 0
    # 합집합이 0이라면(집합1과 2가 공집합이라면)
    if len(union) == 0:
        answer = 1
    # 교집합이 없다면
    elif len(intersection) == 0:
        answer = 0
    else:
        answer = len(intersection) / len(union)
    return int(answer * 65536)
