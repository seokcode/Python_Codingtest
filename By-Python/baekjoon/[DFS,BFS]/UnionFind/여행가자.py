N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]
  
def union(x,y):
  x = find(x)
  y = find(y)
  if x == y:
    return
  else:
    parent[max(x,y)] = min(x,y)

for x in range(1, N+1):
  link = list(map(int,input().split()))
  for y in range(1, N+1):
    if link[y-1] == 1:
      union(x,y)

visit = list(map(int,input().split()))
result = [find(i) for i in visit]

if len(set(result)) == 1:
  print('YES')
else: 
  print('NO')