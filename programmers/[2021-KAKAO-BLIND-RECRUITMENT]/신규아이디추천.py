# 신규 아이디 추천

import re


def solution(new_id):
    new_id = new_id.lower()  # step1
    new_id = re.sub('[\\[\\]~!@#$%^&*()=+{}:?,<>/]', '', new_id)  # step2
    new_id = re.sub('[.]{2,}', '.', new_id)  # step3

    # step4
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # step5
    if len(new_id) == 0:
        new_id = 'a'

    # step6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # step7
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id