class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        soma, somaaux = 0, 0
        for k in words:
            for j in k:
                for i in range(len(allowed)):
                    if allowed[i] == j:
                        somaaux += 1
            if somaaux == len(k):
                soma += 1
            somaaux = 0
        return soma
        