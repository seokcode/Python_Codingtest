# 스택 수열 # B_1874

how_long=int(input())
stk=[]
op=[]
status=True
count=1

for i in range(how_long):
    num=int(input())
    while count<=num:
            stk.append(count)
            op.append('+')
            count+=1
    if stk[-1]==num:
        stk.pop()
        op.append('-')
    else:
        status=False
if status==False:
    print('NO')
else:
    for i in op:
        print(i)