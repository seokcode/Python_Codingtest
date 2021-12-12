class Solution {
    func isValid(_ s: String) -> Bool {
        guard !s.isEmpty else { return true }
        var stack: [Character] = []
    
        for bracket in s {
            switch bracket {
                case "{":
                stack.append("}")
                case "(":
                stack.append(")")
                case "[":
                stack.append("]")
                default:
                    guard bracket == stack.popLast() else { return false }
            }
        }
        return stack.isEmpty
    }
}