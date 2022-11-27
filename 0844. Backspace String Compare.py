class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack_s = []
        stack_t = []
        
        for idx in range(len(s)):
            if s[idx] != '#':
                stack_s.append(s[idx])
            else:
                if len(stack_s) == 0:
                    pass
                else:
                    stack_s.pop()
        
        for idx in range(len(t)):
            if t[idx] != '#':
                stack_t.append(t[idx])
            else:
                if len(stack_t) == 0:
                    pass
                else:
                    stack_t.pop()

        output = True if stack_s == stack_t else False
        return output
