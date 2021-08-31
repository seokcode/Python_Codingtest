import Foundation

func toMiliSec(_ str: String) -> Int {
    let times = str.split(separator: ":").map{Float(String($0))!}
    return Int((times[0] * 3600 + times[1] * 60 + times[2])*1000)
}

// 입력받은 start로부터 1초라는 범위 내에 속한 log가 몇개인지 count
func checkTraffic(_ start: Int, _ logs: [(Int, Int)] ) -> Int {
    var traffic = 0
    let end = start + 1000
    
    // log[0] = 시작시간, log[1] = 끝시간
    // log가 범위내에 속해있으려면 시작시간이 end 미만이어야하고 끝시간이 start 이상이어야한다
    // 걸쳐있는경우도 있기 때문
    logs.forEach {
        if $0.1 >= start && end > $0.0 {
            traffic += 1
        }
    }
    
    return traffic
}

func solution(_ lines:[String]) -> Int {
    // 트래픽은 최소 1개
    var answer = 1
    var logs = [(Int, Int)]()
    
    for l in lines {
        let info = l.split(separator: " ").map{(String($0))} 
        // 종료시간
        let end = toMiliSec(info[1])
        // 트래픽 처리 시간
        let prcTime = Int(Float(info[2].replacingOccurrences(of: "s", with: ""))!*1000)
        // 시작시간 = 종료시간-트래픽처리시간+0.001초
        let start = end - prcTime + 1
        // lines배열이 시간순으로 들어있기 때문에 시간이 빠른 순서대로 저장됨
        logs.append((start,end))
    }
    // 시간이 빠른 순서대로 최대처리트래픽 도출시키기    
    logs.forEach { answer = max(answer, checkTraffic($0.0, logs), checkTraffic($0.1, logs)) }
    
    return answer
}

