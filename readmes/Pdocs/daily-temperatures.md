# Daily Temperatures
> **Medium**
>
> **2022-01-16**
>
> **[Leetcode: Daily Temperatures](https://leetcode.com/problems/daily-temperatures)**


## Sol 

주어진 Temperatures 배열은 연속적인 날들의 온도를 기록한 배열이다.

배열이 주어지면 오늘을 기준으로 오늘보다 따뜻해지려면 며칠을 기다려야하는지 연산하여 return 해주어야한다. 

#### Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```
직접해보기

## 답안
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 답은 temperatures배열의 크기와 같음
        ans = [0]*len(temperatures) 
        stack = []

        for i,v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index 
            stack.append([i,v])      

        return ans
```