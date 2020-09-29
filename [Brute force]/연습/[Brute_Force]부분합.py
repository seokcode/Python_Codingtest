# 부분합 # B_1860
# 일부 경우만 해보기

n,s = map(int,input().split())
a = list(map(int,input().split()))
left = right = 0
sum = a[0]
ans = []

while left <= right and right < n:  # l은 항상 r보다 작고 r은 항상 n(수의 갯수)보다 작음
    if sum < s:  # sum이 목표 숫자보다 작으면 r 증가
        right += 1
        if right < n:  # r이 n 미만이면 sum에 추가
            sum += a[right]
    elif sum >= s:  # 목표 숫자보다 크거나 같아짐
        ans.append(right-left+1)  # 문자열의 길이 push
        sum -= a[left]  # l 담당 숫자 제거하고 l 증가
        left += 1
        if left > right and left < n:  # l이 r보다 커져버리면
            right = left
            sum = a[left]
if not ans:
    print(0)
else:
    print(min(ans))  # 문자열 길이 최솟값 출력

