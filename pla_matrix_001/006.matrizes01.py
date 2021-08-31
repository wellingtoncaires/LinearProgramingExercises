from functions.createdFunctions import create
from functions.createdFunctions import show

print()
print("01. Construir matriz A = 3x2, tal que {1, se i = j & i², se i != j}")

matrix = create(3, 2)
for i in range(0, 3):
    for j in range(0, 2):
        if i == j:
            matrix[i].append(1)
        else:
            iaux = i + 1
            matrix[i].append(iaux * iaux)
print(f"\n{'Resultado':^16}")
show(matrix)
