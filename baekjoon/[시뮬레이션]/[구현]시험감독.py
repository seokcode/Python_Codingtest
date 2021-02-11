# 시험 감독 # B_13458

n = int(input())
a = input().split()
b,c = map(int, input().split())

ans = n
for i in range(n):
  if (int(a[i])-b) <= 0:
      continue
  else:
    if ((int(a[i])-b) % c) == 0:
      ans += ((int(a[i])-b) // c)
    else:
      ans += ((int(a[i])-b) // c)+1

print(ans)