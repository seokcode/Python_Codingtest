import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var row = 0
    var col = 0
    for size in sizes {
		row = max(row, size.max()!)
        col = max(col, size.min()!)
    }
    
    return row * col
}