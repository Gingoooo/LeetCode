class Solution:
    def romanToInt(self, s: str) -> int:
        hash_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        hash_2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        total = 0
        for k2 in hash_2.keys():
            if k2 in s:
                time = s.count(k2)
                s = s.replace(k2, '_')
                total += hash_2[k2] * time
        for k1 in hash_1.keys():
            if k1 in s:
                k1
                time = s.count(k1)
                s = s.replace(k1, '')
                total += hash_1[k1] * time
        return total