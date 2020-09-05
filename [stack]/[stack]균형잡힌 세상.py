# 균형잡힌 세상 # B_4949

while 1:
    question=input()

    if question=='.':
        break

    q_stack=[]
    temp=True
    for j in question:
        if j=='(' or j=='[':
            q_stack.append(j)
        elif j==')':
            if not q_stack or q_stack[-1]=='[':
                temp=False
                break
            elif q_stack[-1]=='(':
                q_stack.pop()
        elif j == ']':
            if not q_stack or q_stack[-1] == '(':
                temp = False
                break
            elif q_stack[-1] == '[':
                q_stack.pop()

    if temp==True and not q_stack:
        print('yes')
    else:
        print('no')