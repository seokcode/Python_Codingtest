# Multiply Strings
> **Medium**
>
> **2021-08-18**
>
> **[Leetcode: 43. Multiply Strings](https://leetcode.com/problems/multiply-strings)**


## Sol

주어지는 문자열 형태의 숫자를 서로 곱한 결과를 return해야하는 간단한 문제.

하지만 주어지는 문자열을 바로 정수형으로 변환해서는 안된다. 

0의 아스키 코드를 기준으로 아스키 코드 또한 1씩 증가한다는 점을 활용하여 아스키 코드 변환을 통해 문제를 풀어주었다.
> ord('0') = 48 / ord('1') = 49 ...


## 답안
```swift
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
```