# Runtime: 232 ms, faster than 85.87% of Python3 online submissions for Binary Search.
# Memory Usage: 15.5 MB, less than 69.92% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left ,right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left) //2
            
            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1
            