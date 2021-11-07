# Runtime: 52 ms, faster than 57.48% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.9 MB, less than 81.94% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + ((right-left) // 2)
            
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left