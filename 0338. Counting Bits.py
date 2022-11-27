class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def ten_trans_bin(num):
            if n < 2:
                return num
            list_o = []
            while True:
                list_o.append(num % 2)
                num = num // 2
                if num < 2:
                    list_o.append(num)
                    break 
            return sum(list_o)
        
        output = []
        for i in range(n+1):
            output.append(ten_trans_bin(i))

        return output