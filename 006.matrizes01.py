from createdFunctions import create

print()
print("01. Construit matriz A = 3x2, tal que {1, se i = j & i², se i != j}")

matriz = create(3, 2)
for i in range(0, 3):
    for j in range(0, 2):
        if i == j:
            matriz[i].append(1)
        else:
            iaux = i + 1
            matriz[i].append(iaux * iaux)

for i in range(0, 3):
    for j in range(0, 2):
        print(matriz[i][j], end="   ")
    print()