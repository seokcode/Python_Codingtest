N = int(input())
A = list(map(int, input().split()))

stack = [0]
answer = [-1] * len(A)
for i in range(1, len(A)):
  while stack and A[stack[-1]] < A[i]:
    answer[stack.pop()] = A[i]
  stack.append(i)

print(*answer)
