class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures) 
        stack = []

        for i,v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index,value = stack.pop()
                ans[index] = i - index 
            stack.append([i,v])      

        return ans