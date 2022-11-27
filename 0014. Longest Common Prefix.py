class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        # 最短長度 alpha
        len_min_words = min([len(n) for n in strs])
        for idx in range(len_min_words):
            if len(set([n[idx] for n in strs])) == 1:
                output += strs[0][idx]
            else:
                break
        return output