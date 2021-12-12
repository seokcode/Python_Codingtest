import Foundation
let sounds = readLine()!
let pattern = "\\b(100+1+|01)+\\b"
let regex = try? NSRegularExpression(pattern: pattern)
if let isMatch = regex?.matches(in: sounds, options: [], range: NSRange(location: 0, length: sounds.count)).isEmpty {
    isMatch ? print("NOISE") : print("SUBMARINE")
}