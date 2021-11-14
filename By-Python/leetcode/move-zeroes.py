class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        noneZeroArr = list(filter(lambda x: x != 0, nums))
        nums[:] = noneZeroArr + (len(nums) - len(noneZeroArr))*[0]
        """
        Do not return anything, modify nums in-place instead.
        """