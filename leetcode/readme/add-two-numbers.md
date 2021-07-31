# Add Two Numbers
> **Medium**
>
> **2021-07-31**
>
> **[Leetcode: Add Two Numbers](https://leetcode.com/problems/add-two-numbers)**


## Sol
Linked List를 활용해야 하는 문제였다.  

l1,l2가 주어지는데 예를 들어 l1이 [2,4,3]일 경우 l1.val은 `2` l1.next는 `ListNode{val: 4, next: ListNode{val: 3, next: None}}`이다.

그리고 l1,l2에 각각 숫자가 본래의 역순으로 들어가 있기 때문에 2,4,3은 2+40+300과 같음을 이용하여 문제를 풀어주었다.

return값 또한 ListNode여야 하므로 이를 주의해야한다.

## 답안
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = 1
        total = 0
        while l1 or l2:
            l1_val,l2_val = 0, 0
            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next
            
            total += (l1_val+l2_val)*num
            num *= 10
        
        header=None
        result=None
        for c in str(total):
            if not header:
                header=ListNode(int(c))
                result=header
            else:
                curNode=ListNode(int(c),result)
                result=curNode
        
        return result
```