# 주식

for _ in range(int(input())):
  days = int(input())
  stocks = list(map(int, input().split()))
  answer = 0
  max_cost = stocks[-1]

  for i in range(days-2,-1,-1):
    if stocks[i] > max_cost:
      max_cost = stocks[i]
    else:
      answer += (max_cost-stocks[i])

  print(answer)

