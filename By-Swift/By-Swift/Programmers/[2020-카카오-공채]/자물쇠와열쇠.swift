import Foundation

// 열쇠 회전
func turn(_ key: [[Int]]) -> [[Int]] {
    var turnKey = Array(repeating: [Int](), count: key.count)
    
    for k in key.reversed() {
        for (idx, item) in k.enumerated() {
            turnKey[idx].append(item)
        }
    }
    
    return turnKey
}

// 열쇠가 구멍에 맞는지 확인
func check(_ key:[[Int]],_ locksize: Int, _ lock:[[Int]], _ x: Int, _ y: Int) -> Bool {
    var keySize = key.count
    var compare = lock
    
    // 열쇠구멍에 열쇠 넣어보기
    for i in 0..<keySize {
        for j in 0..<keySize {
            compare[i+x][j+y] = key[i][j] + lock[i+x][j+y]
        }
    }
    
    // 맞는지 확인하기
    for i in 0..<locksize {
        for j in 0..<locksize {
            if compare[keySize-1+i][keySize-1+j] != 1 {
                return false
            }
        }
    }
    
    return true
}

func solution(_ key:[[Int]], _ lock:[[Int]]) -> Bool {
    let size = lock.count + (key.count*2) - 2
    var expandedLock = Array(repeating: Array(repeating: Int(), count: size), count: size)
    var key = key
    
    var row = key.count-1
    let col = key.count-1
    for i in lock {
        for (idx,j) in i.enumerated() {
            expandedLock[row][col+idx] = j
        }
        row += 1
    }
    
    // 90도 4번 = 360도
    for _ in 0..<4 {
        // lock과 딱 한 칸만 겹치는 경우가 최대 길이이므로
        // 최대 길이는 { len(key) -1 } * 2 + len(lock)과 같다.
        for x in 0...(size-key.count) {
            for y in 0...(size-key.count) {
                if check(key, lock.count, expandedLock, x, y) {
                    return true
                }
            }
        }
        key = turn(key)
    }
    
    return false
}