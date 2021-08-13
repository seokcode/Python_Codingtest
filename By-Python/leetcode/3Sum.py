class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = set(), len(nums)        
        nums.sort()
 
        for i in range(n) :
            # 바로 이전 고정값과 같다면 패스(정렬되어있기 때문에 같은 숫자끼리는 붙어있음)
            if i > 0 and nums[i] == nums[i-1] :
                continue
 
            # 범위 지정해서 탐색
            j, r = i+1, n-1 
            while j < r:
                s = nums[i] + nums[j] + nums[r]
                # 합이 0에 못미친다면 j(left) 포인터를 우로 한 칸 이동(더 큰 숫자를 향해)
                if s < 0:
                    j +=1 
                # 합이 0을 초과한다면 r(right) 포인터를 좌로 한 칸 이동(더 작은 숫자를 향해)
                elif s > 0:
                    r -= 1
                # 합이 0이라면 해당 triplet 추가
                else:
                    res.add((nums[i], nums[j], nums[r]))
                    j += 1; r -= 1
        return list(res)
                