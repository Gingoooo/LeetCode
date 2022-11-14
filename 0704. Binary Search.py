class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1 
            else: # target < nums[mid]:
                left = mid + 1
        return -1
        