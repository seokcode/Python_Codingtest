//
//  keys-and-rooms.swift
//  Algorithm-Swift
//
//  Created by 이원석 on 2021/04/14.
//


// Runtime: 236 ms, faster than 5.56% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.5 MB, less than 24.31% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var v: Array<Int> = [0]
            
        func visit(_ keys: [Int]) {
            for i in keys{
                if !v.contains(i) {
                    v.append(i)
                    visit(rooms[i])   
                }                
            }
        }
        
        visit(rooms[0])
        
        if v.count != rooms.count {
            return false
        }else{
            return true
        }
    }
}

// Runtime: 36 ms, faster than 98.61% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.9 MB, less than 8.33% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var v: Set<Int> = [0]
            
        func visit(_ keys: [Int]) {
            for i in keys{
                if !v.contains(i) {
                    v.insert(i)
                    visit(rooms[i])   
                }                
            }
        }
        
        visit(rooms[0])
        
        if v.count != rooms.count {
            return false
        }else{
            return true
        }
    }
}


// Runtime: 32 ms, faster than 100.00% of Swift online submissions for Keys and Rooms.
// Memory Usage: 14.1 MB, less than 83.33% of Swift online submissions for Keys and Rooms.
class Solution {
    func canVisitAllRooms(_ rooms: [[Int]]) -> Bool {
        var keys: [Int] = Array(repeating: -1, count: rooms.count)
        keys[0] = 0
        var visited = [0]
        var num = 0
        
        while num < visited.count {
            for i in rooms[visited[num]]{
                if keys[i] == -1 {
                    keys[i] = 0
                    visited.append(i)
                }
            }
            if visited.count == rooms.count{
                return true
            }else{
                num += 1   
            }
        }
        
        return false
    }
}