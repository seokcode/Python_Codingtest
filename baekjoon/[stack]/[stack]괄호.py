# B_9012
case_num=int(input())
result=[]

for i in range(case_num):
    question=list(input())
    q_stack=[]
    temp=True
    for j in question:
        if j=='(':
            q_stack.append(j)
        elif j==')':
            if not q_stack:
                temp=False
                break
            elif q_stack[-1]=='(':
                q_stack.pop()
    if temp==True and not q_stack:
        print('YES')
    else:
        print('NO')