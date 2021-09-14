import Foundation

var answer = 0

func test(_ cnt: Int, _ spend: Int, _ remain: Int, _ wallet: [Int], _ total: Int, _ NTK: (Int,Int,Int)) -> Bool {
    var wallet = wallet
    var total = total
    
    wallet.append(spend)
    total += spend
    
    if wallet.count > NTK.1 {
        total -= wallet.removeFirst()
    }
    if total > NTK.2 || (cnt >= NTK.0 && remain != 0){
        return false
    }
    
    if cnt == NTK.0 && remain == 0 && total <= NTK.2 {
        return true
    }
    
    for i in 0...remain {
        if test(cnt+1, i, remain-i, wallet, total, NTK) {
            answer += 1
        }
    }
    
    return false
}

func solution(_ n: Int, _ money: Int, _ T: Int, _ K: Int ) -> Int {
    for i in 0...K {
        // Cnt, Spend, Remain, Wallet, Total, NTK
        test(1, i, money-i, [Int](), 0, (n, T, K))
    }
    
    return answer
}


print(solution(4, 7, 2, 4))
//4 7 2 4 /// 28

/**
ATM기기의 갯수 N,
총 넣어야 할 돈 money,
연속된 ATM T,
ATM에 돈을 넣을 때 T 범위 안에서는 최대 K만큼만 넣을 수 있다.

N: 4, money: 7, T: 2, K: 4 이면 아래처럼 28개 경우

[0, 3, 0, 4]
[0, 3, 1, 3]
[0, 4, 0, 3]
[1, 2, 0, 4]
[1, 2, 1, 3]
[1, 2, 2, 2]
[1, 3, 0, 3]
[1, 3, 1, 2]
[2, 1, 0, 4]
[2, 1, 1, 3]
[2, 1, 2, 2]
[2, 1, 3, 1]
[2, 2, 0, 3]
[2, 2, 1, 2]
[2, 2, 2, 1]
[3, 0, 0, 4]
[3, 0, 1, 3]
[3, 0, 2, 2]
[3, 0, 3, 1]
[3, 0, 4, 0]
[3, 1, 0, 3]
[3, 1, 1, 2]
[3, 1, 2, 1]
[3, 1, 3, 0]
[4, 0, 0, 3]
[4, 0, 1, 2]
[4, 0, 2, 1]
[4, 0, 3, 0]
*/
