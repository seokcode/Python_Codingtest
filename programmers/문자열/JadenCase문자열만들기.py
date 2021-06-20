import re

def solution(s):
    separateItem = s.split(" ") 
    answer = []
    for (idx,item) in enumerate(separateItem):
        if item == "":
            continue
            
        item = list(item.lower())
        if re.findall('[a-zA-Z]',item[0]):
            item[0] = item[0].upper()
        separateItem[idx] = "".join(item)
        
    return " ".join(separateItem)