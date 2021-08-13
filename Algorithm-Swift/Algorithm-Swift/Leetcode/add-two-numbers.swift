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

 // Sol 1
class Solution {    
    fileprivate var anchor = 0
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        if l1 == nil && l2 == nil && anchor == 0 { return nil }
        
        let sum = (l1?.val ?? 0) + (l2?.val ?? 0) + anchor
        anchor = sum / 10
        return .init(sum % 10, addTwoNumbers(l1?.next, l2?.next))
    }     
}


// Sol 2
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