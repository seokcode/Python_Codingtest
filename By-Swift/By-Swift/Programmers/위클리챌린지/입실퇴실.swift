import Foundation

func solution(_ enter:[Int], _ leave:[Int]) -> [Int] {
    var answer = Array(repeating: 0, count: enter.count)
    var room = [Int]()
    var head = 0
    
    for l in leave {
        while !room.contains(l) {
            room.append(enter[head])
            head += 1
        }
        
        room = room.filter{$0 != l}
        answer[l-1] += room.count
        
        for r in room {
            answer[r-1] += 1
        }
    }
    
    return answer
}