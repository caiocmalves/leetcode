class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = nums
        for i in range(0, len(nums)):
            ans.append(nums[i])
        return ans