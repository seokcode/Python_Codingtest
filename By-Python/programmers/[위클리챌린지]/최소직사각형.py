def solution(sizes):
    
    rows,cols = 0,0
    for r,c in sizes:
        row = max(r,c)
        col = min(r,c)
        rows = max(rows, row)
        cols = max(cols, col)
    
    return rows * cols