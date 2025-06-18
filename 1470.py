class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new = []
        for i in range(int(len(nums) / 2)):
            new.append(nums[i])
            new.append(nums[i+n])
        return new
        