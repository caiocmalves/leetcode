class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        for i in candies:
            if i + extraCandies < max(candies):
                result.append(False)
            else:
                result.append(True)
        return result