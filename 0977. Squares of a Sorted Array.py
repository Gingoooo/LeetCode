class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = sorted([n ** 2 for n in nums])
        return output