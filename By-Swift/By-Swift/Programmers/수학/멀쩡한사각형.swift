import Foundation

func euclidean(_ big: Int, _ small: Int) -> Int {
    if big % small == 0 {
        return small
    } else {
        return euclidean(small, big%small)
    }
}

func solution(_ w:Int, _ h:Int) -> Int64{
    var width = w
    var height = h
    if w == h { return Int64((w*h)-w) }
    if h > w { (width, height) = (height, width) }
    
    return Int64((width*height) - (w+h-euclidean(width,height)))
}