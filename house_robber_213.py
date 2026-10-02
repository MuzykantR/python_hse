class Solution:
    def rob(self, nums: list[int]) -> int:
        def line(arr: list[int]) -> int:
            if len(arr) == 1:
                return arr[0]
            best = [0] * len(arr)
            best[0] = arr[0]
            best[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                best[i] = max(arr[i] + best[i - 2], best[i - 1])
            return best[-1]

        if len(nums) == 1:
            return nums[0]
        
        return max(line(nums[:-1]), line(nums[1:]))