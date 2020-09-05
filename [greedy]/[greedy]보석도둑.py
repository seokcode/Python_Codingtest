# 보석 도둑 # B_1202
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

# 보석의 무게와 가치를 heap에 저장
gem = []
for i in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gem, [weight, value])

# 가방 최대 용량을 저장 후 오름차순 정렬
bag = []
for i in range(K):
    bag.append(int(input()))

bag.sort()

result = 0
capable_gem = []  # 가방에 들어갈 수 있는 무게의 보석 저장 리스트
for i in range(K):
    # gem이 비어있지 않고 가방의 용량이 보석의 무게를 감당 가능 할 때
    # 보든 보석에 대하여
    while gem and bag[i] >= gem[0][0]:
        # gem에서 pop하여 weight, value 에 heappop한 값 저장
        [weight, value] = heapq.heappop(gem)
        # capable_gem에 값어치 순으로 최대힙정렬
        heapq.heappush(capable_gem, -value)

    # capable_gem이 있다면 result에 추가
    if capable_gem:
        result += -(heapq.heappop(capable_gem))
    elif not gem:  # 남은 보석이 한 개도 없는 경우
        break

print(result)