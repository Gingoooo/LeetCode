class Solution:
    def findLucky(self, arr: List[int]) -> int:
        output = -1
        hash_table = {}
        for a in arr:
            if a in hash_table.keys():
                hash_table[a] = hash_table[a]+1
            else:
                hash_table[a] = 1
        for k, v in hash_table.items():
            if (k == v) and (output < v):
                output = v
        return output