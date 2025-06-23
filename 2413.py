class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        cont = 0
        while True:
            cont += 1
            if cont % 2 == 0 and cont % n == 0:
                break
        return cont
