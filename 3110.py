class Solution:
    def scoreOfString(self, s: str) -> int:
        cont = 0
        for i in range(len(s)):
            if i == 0:
                continue
            cont += abs(ord(s[i - 1]) - ord(s[i]))
        return cont
        