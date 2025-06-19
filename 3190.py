class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        op = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 2 or nums[i] % 3 == 1:
                op += 1
        return op