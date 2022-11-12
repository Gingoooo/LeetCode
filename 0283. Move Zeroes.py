class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = nums.count(0)
        for i in range(count_0):
            nums.remove(0)
            nums.append(0)
