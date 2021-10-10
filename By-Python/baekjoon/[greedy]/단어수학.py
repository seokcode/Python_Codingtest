from collections import defaultdict

N = int(input())
archive = defaultdict(int)
answer = 0

for _ in range(N):
  word = input()
  wordLen = len(word)
  for i in range(wordLen):
    archive[word[i]] += 10**(wordLen-i-1)

valueList = list(archive.values())
valueList.sort(reverse=True)
numbers = list(range(10))

for v in valueList:
  answer += v*(numbers.pop())

print(answer)