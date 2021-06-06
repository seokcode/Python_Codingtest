# 랜선 자르기

k, n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
start, end = 1, max(arr)

while start <= end:
  mid = (start+end)//2
  lines = 0
  for lan in arr:
    lines += lan//mid
  
  if lines >= n:
      start = mid + 1
  else:
      end = mid - 1

print(end)