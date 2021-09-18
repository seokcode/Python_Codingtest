def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    enterHead = 0
    leaveHead = 0
    
    while enterHead < len(enter) and leaveHead < len(leave):
        room.append(enter[enterHead])
        enterHead += 1       
        
        while leaveHead < len(leave) and leave[leaveHead] in room:
            room.remove(leave[leaveHead]) # 퇴장
            answer[leave[leaveHead]-1] += len(room) # 퇴장한 사람이 퇴장 전에 같이 있던(만난) 인원 수
            leaveHead += 1
            
            # 퇴장 이후 남은 사람들도 퇴장한 사람 만났었던거니까 +1
            for r in room:
                answer[r-1] += 1
        
    return answer