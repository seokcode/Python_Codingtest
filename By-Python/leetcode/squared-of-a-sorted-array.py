# Runtime: 232 ms, faster than 67.44% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 15.8 MB, less than 91.16% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2, nums)))
        