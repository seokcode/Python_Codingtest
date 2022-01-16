# Rotate Image
> **Easy**
>
> **2022-01-16**
>
> **[Leetcode: Rotate Image](https://leetcode.com/problems/rotate-image)**


## Sol 

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

## 답안
> Runtime: 20 ms, faster than 99.92% of Python3 online submissions for Rotate Image.  
> Memory Usage: 14.1 MB, less than 85.64% of Python3 online submissions for Rotate Image.
```python
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
```

## 다른 방법
```python
# 1
class Solution:
    def rotate(self, A):
        A[:] = map(list, zip(*A[::-1]))

# 2
class Solution:
    def rotate(self, A):
        A[:] = [[row[i] for row in A[::-1]] for i in range(len(A))]

# 3
class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
```