# Add Two Numbers
> **Medium**
>
> **2021-08-13**
>
> **[Leetcode: Add Two Numbers](https://leetcode.com/problems/add-two-numbers)**


## Sol
Linked List를 활용해야 하는 문제였다.  

l1,l2가 주어지는데 예를 들어 l1이 [2,4,3]일 경우 l1.val은 `2` l1.next는 `ListNode{val: 4, next: ListNode{val: 3, next: None}}`이다.

합이 10 이상일 경우 올림수가 발생하므로 10의 몫 만큼 올림수로 저장해준뒤 10의 나머지를 더해주었다.
(ex 15라면 올림수는 1(`15/10`) 올림수를 제외하고 더해줘야하는 숫자 5(`15%10`))

return값 또한 ListNode여야 하므로 이를 주의해야한다.

## 답안 1
```swift
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {    
    fileprivate var anchor = 0
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        if l1 == nil && l2 == nil && anchor == 0 { return nil }
        
        let sum = (l1?.val ?? 0) + (l2?.val ?? 0) + anchor
        anchor = sum / 10
        return .init(sum % 10, addTwoNumbers(l1?.next, l2?.next))
    }     
}
```

```swift
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?, didCarry: Bool = false) -> ListNode? {
        guard let l1 = l1 else {
            return didCarry ? addTwoNumbers(ListNode(1), l2) : l2
        }

        guard let l2 = l2 else {
            return didCarry ? addTwoNumbers(l1, ListNode(1)) : l1
        }

        let nextVal = l1.val + l2.val + (didCarry ? 1 : 0)
        let shouldCarry = nextVal > 9

        let resultNode = ListNode(shouldCarry ? nextVal - 10 : nextVal)
        resultNode.next = addTwoNumbers(l1.next, l2.next, didCarry: shouldCarry)

        return resultNode
    }
}
```