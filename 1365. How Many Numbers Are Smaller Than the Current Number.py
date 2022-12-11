class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        o_nums = []
        nums_ = nums.copy()
        for n in nums:
            counts = 0
            for n_ in nums_:
                if n > n_:
                    counts += 1
            o_nums.append(counts)
        return o_nums