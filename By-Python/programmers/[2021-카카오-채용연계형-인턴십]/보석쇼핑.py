def solution(n, k, cmd):
    table = ["O" for _ in range(n)]
    linked = {i: [i-1,i+1] for i in range(1,n+1)}
    clipboard = []
    cur = k+1
    
    for c in cmd:
        if c[0] == "D":
            for _ in range(int(c[2:])):
                cur = linked[cur][1]
        
        if c[0] == "U":
            for _ in range(int(c[2:])):
                cur = linked[cur][0]
        
        if c[0] == "C":
            table[cur-1] = "X"
            pre, nxt = linked[cur]
            clipboard.append([pre,nxt,cur])
            
            if pre != 0:
                linked[pre][1] = linked[cur][1] 
            if nxt != n+1:
                linked[nxt][0] = linked[cur][0]

            if nxt == n+1:
                cur = linked[cur][0] 
            else:
                cur = linked[cur][1] 
            
        if c[0] == "Z":
            pre,nxt,restore = clipboard.pop()
            table[restore-1] = "O"
            
            if pre != 0:
                linked[pre][1] = restore
            if nxt != n+1:
                linked[nxt][0] = restore
            
    return "".join(table)