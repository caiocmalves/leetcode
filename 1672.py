class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        soma = 0
        wealth = 0
        for i in accounts:
            soma = 0
            for j in i:
                soma += j
            if soma > wealth:
                wealth = soma
        return wealth
        