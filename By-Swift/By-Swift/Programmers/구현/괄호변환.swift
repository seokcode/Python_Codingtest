import Foundation

func balance(_ bal: String) -> Bool {
    var stack: [String] = []
    for b in bal {
        if b == "(" { 
            stack.append("(")
        } else { 
            if stack.last == "(" {
                stack.removeLast()
            } else {
                return false
            }
        }
    }
    return true
}

func solution(_ p:String) -> String {
    var count = 0
    var index = p.startIndex
    
    if p.count < 1 { return "" }
    
    while true {
        count += String(p[index]) == "(" ? 1 : -1 
        index = p.index(after: index)
        if count == 0 { break }
    }
    var u = String(p[..<index]), v = String(p[index...])
    
    if balance(u) {
        return u + solution(v)
    } else {
        u.removeFirst()
        u.removeLast()
        return "("+solution(v)+")"+u.map{String($0)==")" ? "(" : ")"}
    }
}