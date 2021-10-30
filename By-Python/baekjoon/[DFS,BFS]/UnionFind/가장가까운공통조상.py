T = int(input())

for _ in range(T):
  N = int(input())
  parent = [0 for _ in range(N+1)]
  
  for _ in range(N-1):
    A, B = list(map(int,input().split()))
    parent[B] = A
  
  GA, GB = list(map(int,input().split()))
  rootA, rootB = [GA], [GB]

  while parent[GA]:
    rootA.append(parent[GA])
    GA = parent[GA]

  while parent[GB]:
    rootB.append(parent[GB])
    GB = parent[GB]

  cnt = 1
  while min(len(rootA), len(rootB)) >= cnt:
    if rootA[-cnt] == rootB[-cnt]:
      cnt += 1
    else:
      break
  print(rootA[-cnt+1])