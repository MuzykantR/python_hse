class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        while left <= right:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            mid = left + (right - left) // 2
        
        return -1