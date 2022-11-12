class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic_ran = {}
        for r in ransomNote:
            if r not in dic_ran:
                dic_ran[r] = 1
            else:
                dic_ran[r] += 1
        for m in magazine:
            if m in dic_ran:
                if dic_ran[m] > 1:
                    dic_ran[m] -= 1
                else:
                    del dic_ran[m]
            if len(dic_ran) == 0:
                return True
        if len(dic_ran) > 0:
            return False
        else:
            return True