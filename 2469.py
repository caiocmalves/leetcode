class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = round((celsius + 273.15), 5)
        f = round((celsius * 1.8 + 32),5)
        ans = [k, f]
        return ans