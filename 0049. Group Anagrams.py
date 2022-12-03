class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = {}
        for str_ in strs:
            k = ''.join(sorted(str_))
            if k not in hash_table:
                hash_table[k] = [str_]
            else:
                hash_table[k].append(str_)
        return [v for v in hash_table.values()]