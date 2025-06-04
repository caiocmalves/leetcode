class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for i in range (0, len(nums)):
            output.append(nums[nums[i]])
        return output