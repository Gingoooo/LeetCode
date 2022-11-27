class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for num in nums:
            if num not in hash_table:
                hash_table[num] = 1
        for n in range(len(nums)+1):
            if n not in hash_table:
                return n