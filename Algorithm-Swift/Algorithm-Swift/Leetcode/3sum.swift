class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        var res = Set<[Int]>()
        let n = nums.count
        let numArr = nums.sorted()
        
        for i in 0..<n {
            if i > 0 && numArr[i] == numArr[i-1] {
                continue
            }
            
            var j = i+1
            var r = n-1
            while j < r {
                let s = numArr[i] + numArr[j] + numArr[r]
                if s < 0 {
                    j += 1
                } else if  s > 0 {
                    r -= 1
                } else {
                    res.insert([numArr[i], numArr[j], numArr[r]])
                    j += 1
                    r -= 1
                }
            }
        }
        return Array(res)
    }
}