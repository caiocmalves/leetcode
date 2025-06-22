class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        repete = []
        for i in range(len(nums)):
            x = nums[i]
            del [nums[i]]
            if x in nums:
                if x in repete:
                    pass
                else:
                    repete.append(x)
            nums.insert(i, x)
        return repete