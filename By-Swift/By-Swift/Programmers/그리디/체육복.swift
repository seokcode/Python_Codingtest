import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var answer = n - lost.count
    var lost_stu = Array(repeating: false, count: lost.count)
    var reserve_stu = Array(repeating: false, count: reserve.count)
    
    // 체육복 여벌로 가져온 학생이 도난 당한 경우 체크
    for (ldx,l) in lost.enumerated() {
        for (rdx,r) in reserve.enumerated() {
            if r == l {
                lost_stu[ldx] = true
                reserve_stu[rdx] = true
                answer += 1
            }
        }   
    }
    
    // 체육복 빌려주기 
    for (ldx,l) in lost.enumerated() {
        for (rdx,r) in reserve.enumerated() {
            if abs(r-l) == 1 && !lost_stu[ldx] && !reserve_stu[rdx] {
                lost_stu[ldx] = true
                reserve_stu[rdx] = true
                answer += 1
            }
        }   
    }
    
    return answer
}


// 
import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    // MARK: - 체육복 여벌로 가져온 학생이 도난 당한 경우 체크
    var reserved = reserve.filter{ !lost.contains($0) } 
    var losted = lost.filter{ !reserve.contains($0) }

    var lost_stu = Array(repeating: false, count: losted.count)
    var reserve_stu = Array(repeating: false, count: reserved.count)
    var answer = n - losted.count
    
    // 체육복 빌려주기
    for (ldx,l) in losted.enumerated() {
        for (rdx,r) in reserved.enumerated() {
            if abs(r-l) == 1 && !lost_stu[ldx] && !reserve_stu[rdx] {
                lost_stu[ldx] = true
                reserve_stu[rdx] = true
                answer += 1
            }
        }   
    }
    
    return answer
}