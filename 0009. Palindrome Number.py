class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 有 -, 長度為偶數 都不要
        str_x = str(x)
        if str_x[0] == '-':
            return False
        elif len(str_x) == 1:
            return True
        else:
            l = 0
            r = len(str_x) - 1
            while l < r:
                if str_x[l] != str_x[r]:
                    return False
                else:
                    l += 1
                    r -= 1
        return True