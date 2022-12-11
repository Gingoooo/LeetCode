class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        pt = int(len(nums)/2)
        for i in range(pt):
            output.append(nums[i])
            output.append(nums[pt+i])
        return output