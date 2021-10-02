def canJump(self, nums: List[int]) -> bool:
    lp, rp = 0, 0
    destination = len(nums)-1
    
    while rp < destination:
        if lp > rp:
            return False
        
        furthest = max([i+nums[i] for i in range(lp, rp+1)])
        lp, rp = rp+1, furthest
        
    return True
