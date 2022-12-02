class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_rev = a[::-1]
        b_rev = b[::-1]
        
        if len(a) > len(b):
            b_rev = b_rev + '0' * (len(a)-len(b))
        if len(a) < len(b):
            a_rev = a_rev + '0' * (len(b)-len(a))

        output = ''
        carry = 0

        for i in range(max(len(a), len(b))):
            total = int(a_rev[i]) + int(b_rev[i]) + carry
            carry = 0 if total < 2 else 1
            point = str(total % 2)
            output = output + point
            # print(a_rev[i], b_rev[i], carry, point)
            
        if carry > 0:
            output = output + '1'

        output = output[::-1]
        
        return output