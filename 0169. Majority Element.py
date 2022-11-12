class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ######## hash 解法 ######## 
        # set_nums = set(nums)
        # for num in set_nums:
        #     if nums.count(num) > int(len(nums)/2):
        #         return num
        #     else:
        #         pass
        # return None

        # 參考 https://clay-atlas.com/blog/2022/02/21/leetcode-169-majority-element/
        ######## Moore voting algorithm ########
        k, v = None, 0
        for n in nums:
            if n == k:
                v += 1
            else:
                if v == 0:
                    k = n
                else:
                    v -= 1
        return k

        