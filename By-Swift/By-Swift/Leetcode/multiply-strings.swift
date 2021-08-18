func multiply(_ num1: String, _ num2: String) -> String {
	var num1A = Array(num1)
	var num2A = Array(num2)
	var sum = [Int](repeating: 0, count: num1.count + num2.count)
	for (i, n1) in num1A.enumerated().reversed() {
		for (j, n2) in num2A.enumerated().reversed() {
			guard let digit1 = n2.wholeNumberValue, let digit2 = n1.wholeNumberValue else { return "" }
			let p1 = i + j
			let p2 = i + j + 1
			let val = digit1 * digit2 + sum[p2] // add in carry from before
			sum[p2] = val % 10
			sum[p1] += val / 10
		}
	}
	while let firstSum = sum.first, firstSum == 0 { sum.removeFirst() }
	let res = sum.map ({ String($0) }).joined()
	return res.count > 0 ? res : "0"
}