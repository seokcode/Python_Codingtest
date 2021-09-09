def solution(enroll, referral, seller, amount):
    relation = dict()
    score = {"center" : 0}
    
    for i in range(len(enroll)):
        if referral[i] == "-":
            referral[i] = "center"
        
        relation[enroll[i]] = referral[i]
        score[enroll[i]] = 0
    

    # s: 판매자 , money: 얻은 수익(수수료 떼야 될 금액)
    def dfs(s, money):
        tax = int(money*0.1)
        if tax >= 1:
                score[s] += (money-tax)
        else: 
            score[s] += money
            return

        if s == "center": 
            return
        else: 
            return dfs(relation[s], tax)

        
    for i in range(len(seller)):
        dfs(seller[i], amount[i]*100)
            
    del score["center"]
    return list(score.values())