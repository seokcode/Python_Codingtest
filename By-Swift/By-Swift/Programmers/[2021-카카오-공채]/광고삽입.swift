import Foundation

func toSec(_ str: String) -> Int {
    let times = str.split(separator: ":").map{Int(String($0))!}
    
    return times[0] * 3600 + times[1] * 60 + times[2]
}

func toStr(_ time: Int) -> String {
    let h = time / 3600
    var s = time - (h * 3600)
    let m = (time % 3600) / 60
    s -= m * 60
    
    let hour = h >= 10 ? "\(h)" : "0\(h)"
    let minute = m >= 10 ? "\(m)" : "0\(m)"
    let sec = s >= 10 ? "\(s)" : "0\(s)"
    
    return hour+":"+minute+":"+sec
}

func solution(_ play_time:String, _ adv_time:String, _ logs:[String]) -> String {
    let play_time = toSec(play_time)
    let adv_time = toSec(adv_time)
    var timeline = Array(repeating: 0, count: play_time+1)
    
    for l in logs {
        // [0] = start, [1] = end
        let curPlay = l.split(separator: "-").map{String($0)}
        
        timeline[toSec(curPlay.first!)] += 1
        timeline[toSec(curPlay.last!)] -= 1
    }
    
    for _ in 0..<2 {
        // 처음 루프는 구간 채우기
        // 두번째 루프는 구간 누적
        for p in 1..<play_time {
            timeline[p] += timeline[p-1]
        }
    }

    // 0초부터 광고를 틀었을 경우
    var answer = (0, timeline[adv_time])
    
    for start in 0..<play_time {
        let end = start+adv_time >= play_time ? play_time : start+adv_time
        
        if answer.1 < timeline[end] - timeline[start] {
            answer = (start+1, timeline[end] - timeline[start])
        }
    }
    return toStr(answer.0)
}