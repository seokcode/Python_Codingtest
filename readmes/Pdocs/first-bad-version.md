# First Bad Version
> **Easy**
>
> **2021-11-07**
>
> **[Leetcode: 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)**


## Sol
> 이진탐색을 사용하려면 배열이 오름차순이어야한다. 

isBadVersion이라는 이미 정의된 API를 호출해서 1~n 의 버젼 중 몇번째 버젼이 가장 처음으로 Bad Version이 되었는지 return하는 문제.
> 만약 버젼 3이 첫 Bad Version이면 3 이상의 모든 버젼은 전부 Bad Version이다.

## 답안
> Runtime: 28 ms, faster than 83.68% of Python3 online submissions for First Bad Version.
> Memory Usage: 14.3 MB, less than 44.40% of Python3 online submissions for First Bad Version.
```python
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
```