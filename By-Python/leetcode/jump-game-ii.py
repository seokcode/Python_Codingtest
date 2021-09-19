class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [0] + [float("inf")] * (len(nums)-1)
        
        for idx,i in enumerate(nums):
            for j in range(1,i+1):
                if idx+j < len(nums):
                    steps[idx+j] = min(steps[idx+j], steps[idx]+1)
       
        return steps[-1]