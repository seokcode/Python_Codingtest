def solution(weights, head2head):
    record = []
    
    for me, i in enumerate(head2head):
        win = 0
        game = 0
        heavy = 0
        for enemy,j in enumerate(i):
            if j != "N": 
                game += 1
                if j == "W": 
                    win += 1
                    if weights[enemy] > weights[me]: 
                        heavy += 1
        
        rate = win/game if game > 0 else 0.0
        record.append([rate, heavy, weights[me], me])
    
    answer = sorted(record, key = lambda x: (x[0], x[1], x[2], -x[3]), reverse = True)
    return [i[3]+1 for i in answer]