import Foundation

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
    public var tail: Node?

    func isEmpty() -> Bool {
        return head == nil
    }

    public func append(_ value: T) {
        let newNode = Node(value: value)

        if isEmpty() {
            head = newNode
            tail = head
        } else {
            newNode.previous = tail
            tail?.next = newNode
            tail = newNode
        }
    }

    public func remove(_ node: Node) -> Node {
        let prev = node.previous
        let next = node.next

        if let prev = prev {
            prev.next = next
        } else {
            head = next
        }

        if let next = next {
            next.previous = prev
            return next
        } else {
            tail = prev
            return tail!
        }
    }

    public func reAppend(_ node: Node) {
        let prev = node.previous
        let next = node.next

        if let prev = prev {
            prev.next = node
        } else {
            head?.previous = node
            head = node
        }

        if let next = next {
            next.previous = node
        } else {
            tail?.next = node
            tail = node
        }
    }
}

func solution(_ n:Int, _ k:Int, _ cmd:[String]) -> String {
    var status = Array(repeating: "O", count: n)
    var clipboard: [LinkedListNode<Int>] = []
    let ll = LinkedList<Int>()
    var cur: LinkedListNode<Int>?

    for i in 0..<n {
        ll.append(i)
        if i == k { cur = ll.tail! }
    }

    for c in cmd {
        let command = c.split(separator: " ")

        switch command.first! {
        case "D":
            for _ in 0..<Int(command.last!)! {
                cur = cur?.next
            }
        case "U":
            for _ in 0..<Int(command.last!)! {
                cur = cur?.previous
            }
        case "C":
            if let current = cur {
                clipboard.append(current)
                status[current.value] = "X"
                cur = ll.remove(current)   
            }

        case "Z":
            if let restore = clipboard.popLast() {
                status[restore.value] = "O"
                ll.reAppend(restore)
            }
        default:
            break
        }
    }

    return status.joined()
}