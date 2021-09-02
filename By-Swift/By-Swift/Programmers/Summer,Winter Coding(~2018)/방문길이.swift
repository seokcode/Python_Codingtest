import Foundation

func solution(_ dirs:String) -> Int {
    let d = ["U": (-1,0), "D": (1,0), "R": (0,1), "L": (0,-1)]
    var lines = Set<[Int]>()
    var cur = (0,0)
    
    for dir in dirs {
        let next = (cur.0+d[String(dir)]!.0, cur.1+d[String(dir)]!.1)
        if (-5 <= next.0 && next.0 <= 5) && (-5 <= next.1 && next.1 <= 5) {
            lines.insert([cur.0, cur.1, next.0, next.1])
            lines.insert([next.0, next.1, cur.0, cur.1])
            cur = next
        }
    }
    return lines.count/2
}