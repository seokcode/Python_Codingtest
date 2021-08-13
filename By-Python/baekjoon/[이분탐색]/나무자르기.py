# 나무 자르기
n,m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 1, max(arr)

while start <= end:
  trims = 0
  mid = (start+end)//2
  for t in arr:
    if t-mid >= 0:
      trims += t-mid
  if trims >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)