from itertools import product

def solution(word):
    basic = ['A', 'E', 'I', 'O', 'U']
    storage = []
    
    
    for i in range(1,6):
        for j in product(basic, repeat = i):
            storage.append("".join(str(w) for w in j))
        
    storage.sort()

    return storage.index(word)+1