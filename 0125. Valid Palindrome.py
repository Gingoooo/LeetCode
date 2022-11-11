class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [alpha.lower() for alpha in s if alpha.isalnum()]
        if len(s) <= 1:
            return True
        else:
            left, right = 0, len(s)-1
            for idx in range(int(len(s)/2)):
                if s[left] == s[right]:
                    print(s[right], s[left])
                    right = right - 1
                    left = left + 1
                else:
                    return False
            return True
