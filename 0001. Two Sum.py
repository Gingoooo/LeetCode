class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, n in enumerate(nums):
            if (target - n) not in hash_table.keys():
                hash_table[n] = idx
            else:
                return [hash_table[target - n], idx]