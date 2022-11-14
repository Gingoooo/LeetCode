class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for alpha in s:
            if alpha not in dic:
                dic[alpha] = 1
            else:
                dic[alpha] += 1
        list_even = [n for n in dic.values() if n % 2 == 0]
        list_odds = [n for n in dic.values() if n % 2 == 1]
        
        if len(list_even) > 0:
            e_part = sum(list_even)
        else:
            e_part = 0
        if len(list_odds) > 0:
            o_part = max(list_odds)
        else:
            o_part = 0

        return e_part + o_part