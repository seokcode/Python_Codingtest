# 수들의 합2 # B_2003
# 일부 경우만 해보기
"""
# N제한 10000이라서 전부 다 해보면 O(N^2) 1억이라 다행히 가능은 하지만
# 수가 목표 수보다 커지면 break, -> O(N)만으로도 가능
#   r
# 1 2 3 4 3 2 1 2
# l
"""
n,s = map(int,input().split())
a = list(map(int,input().split()))
left = right = 0
sum = a[0]
ans = 0

while left <= right and right < n:  # l은 항상 r보다 작고 r은 항상 n(수의 갯수)보다 작음
    if sum < s:  # sum이 목표 숫자보다 작으면 r 증가
        right += 1
        if right < n:  # r이 n 미만이면 sum에 추가
            sum += a[right]
    elif sum == s:  # 목포 숫자와 같아짐
        ans += 1  # 답 카운트 +1
        right += 1  # r 증가
        if right < n:
            sum += a[right]
    elif sum > s:  # 목표 숫자보다 커지면
        sum -= a[left]  # l 담당 숫자 제거하고 l 증가
        left += 1
        if left > right and left < n:  # l이 r보다 커져버리면
            right = left
            sum = a[left]
print(ans)

