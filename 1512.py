class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        soma = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    soma += 1
        return soma