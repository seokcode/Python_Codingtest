import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var ans = 0
    let sortA = A.sorted()
    let sortB = B.sorted(by:>)
    
    for (a,b) in zip(sortA, sortB) {
        ans += a*b
    }

    return ans
}