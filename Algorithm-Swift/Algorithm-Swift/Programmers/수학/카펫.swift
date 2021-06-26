import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var y = 3
    var x = 0
    
    while true {
        x = Int((yellow + 2*y - 4) / (y-2))
        if yellow == (x*y - 2*(x+y-2)) {
            if brown == 2*(x+y-2) {
                break
            }
        }
        y += 1
    }
    return [x, y]
}