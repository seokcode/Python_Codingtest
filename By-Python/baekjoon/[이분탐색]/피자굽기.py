D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizzas = list(map(int, input().split()))
answer = -1

# 위층의 사이즈가 자기보다 작으면 어차피 못내려옴
# 그러니까 위층 사이즈와 자신 중 작은걸로 사이즈 통일
for i in range(1,len(oven)):
  oven[i] = min(oven[i-1], oven[i])

# 이분탐색
def binarySearch(left, right, oven, pizza):
  answer = -2
  while left <= right:
    mid = (left+right)//2
    
    if oven[mid] < pizza:
      right = mid-1
    else:
      answer = mid-1
      left = mid+1
  
  return answer

left, right = 0, D-1
for p in pizzas:
  right = binarySearch(left, right, oven, p)

  if right == -2:
    break

print(right+2)
