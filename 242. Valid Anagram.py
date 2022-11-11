class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic_s, dic_t = dict(), dict()
        for alpha in s:
            if alpha not in dic_s:
                dic_s[alpha] = 1
            else:
                dic_s[alpha] += 1
        
        for alpha in t:
            if alpha not in dic_t:
                dic_t[alpha] = 1
            else:
                dic_t[alpha] += 1

        return True if dic_t.items() == dic_s.items() else False