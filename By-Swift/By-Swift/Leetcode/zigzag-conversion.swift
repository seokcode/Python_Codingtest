class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 { return s }
        
        var groups = Array(repeating: "", count: numRows)
        var idx = 0
        var step = 1

        for l in Array(s) {
            groups[idx] += "\(l)"
            
            if idx+step == numRows {
                step = -1
            } else if idx+step < 0 {
                step = 1
            }
            idx += step
        }
        
        return groups.reduce(""){ $0 + $1 }
    }
}