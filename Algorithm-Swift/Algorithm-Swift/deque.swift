public struct Deque<T> {
    private var storage: [T] = []
    
    public init() {}
    
    public init(_ elements: [T]){
        storage = elements
    }
    
    public mutating func frontEnqueue(_ element: T) -> Bool{
        storage.insert(element, at: 0)
        return true
    }
    
    public mutating func backEnqueue(_ element: T) -> Bool{
        storage.append(element)
        return true
    }
    
    public mutating func frontDequeue() -> T? {
        return isEmpty ? nil : storage.removeFirst()
    }
    
    public mutating func backDequeue() -> T? {
        return isEmpty ? nil : storage.remove(at: storage.count - 1)
    }
    
    public var isEmpty: Bool {
        return storage.isEmpty
    }
    
    public var frontPeek: T? {
        return storage.first
    }
    
    public var backPeek: T? {
        return storage.last
    }
}

extension Deque: CustomStringConvertible {
    public var description: String {
        return storage.description
    }
}