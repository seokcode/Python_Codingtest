def solution(dirs):
    lines = set()
    d = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
    x,y = 0,0
    
    for dir in dirs:
        dx, dy = x + d[dir][0], y + d[dir][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            lines.add((x,y,dx,dy))
            lines.add((dx,dy,x,y))
            x, y = dx, dy
        
    return len(lines)//2