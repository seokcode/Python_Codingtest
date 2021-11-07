# Runtime: 28 ms, faster than 83.68% of Python3 online submissions for First Bad Version.
# Memory Usage: 14.3 MB, less than 44.40% of Python3 online submissions for First Bad Version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right-left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left