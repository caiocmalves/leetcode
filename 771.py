jewels = "aA"
stones = "aAAbbbb"
soma = 0
for i in range(len(stones)):
    if stones[i] in jewels:
        soma += 1

print(soma)