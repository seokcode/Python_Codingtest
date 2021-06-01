/*
[링크](https://github.com/raywenderlich/swift-algorithm-club/tree/master/Linked%20List)
[Array vs Linked List](https://woovictory.github.io/2018/12/27/DataStructure-Diff-of-Array-LinkedList/)

Array: 
> 랜덤 액세스 가능 O(1), 삽입/삭제 O(n)
> 제한된 용량, 그래서 stack 영역에 메모리 할당 됨

Linked List:
> 맨 앞,뒤에서 삭제/삽입 O(1), 원소 접근 O(n), 원하는 곳에 삭제/삽입 O(n)
> 제한되지 않은 용량, 그래서 heap 영역에 메모리 할당 됨


*/

public class LinkedListNode<T> {
    var value: T
    var next: LinkedListNode?
    weak var previous: LinkedListNode?

    public init(value: T) {
        self.value = value
    }
}

public class LinkedList<T> {
    public typealias Node = LinkedListNode<T>
    private var head: Node?

    public var isEmpty: Bool {
        return head == nil
    }

    public var first: Node? {
        return head
    }

    public var last: Node? {
        guard var node = head else {
            return nil
        }
    
        while let next = node.next {
            node = next
        }
        return node
    }

    public func append(value: T) {
        let newNode = Node(value: value)
        if let lastNode = last {
            newNode.previous = lastNode
            lastNode.next = newNode
        } else {
            head = newNode
        }
    }

    public var count: Int {
        guard var node = head else {
            return 0
        }
        
        var count = 1

        while let next = node.next {
            node = next
            count += 1
        }
        return count
    }

    public func insert(_ node: Node, atIndex index: Int) {
        let newNode = node
        if index == 0 {
            newNode.next = head                      
            head?.previous = newNode
            head = newNode
        } else {
            let prev = self.node(atIndex: index-1)
            let next = prev.next

            newNode.previous = prev
            newNode.next = prev.next
            prev.next = newNode
            next?.previous = newNode
        }
    }

    public func removeAll() {
        head = nil
    }

    public func remove(node: Node) -> T {
        let prev = node.previous
        let next = node.next

        if let prev = prev {
            prev.next = next
        } else {
            head = next
        }
        next?.previous = prev

        node.previous = nil
        node.next = nil
        return node.value
    }

    public func removeLast() -> T {
        assert(!isEmpty)
        return remove(node: last!)
    }

    public func removeAt(_ index: Int) -> T {
        let node = nodeAt(index)
        assert(node != nil)
        return remove(node: node!)
    }
}