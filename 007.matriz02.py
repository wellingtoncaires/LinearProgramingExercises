from createdFunctions import create
from createdFunctions import show


print("Seja a matriz A = 3x4, tal que {i+j, se i = j  &  2i - 2j, i != j}. Qual o valor de a22 + a34?")
print()
matrix = create(3, 4)
a22 = 0
a34 = 0
for i in range(0, 3):
    for j in range(0, 4):
        iaux = i + 1
        jaux = j + 1
        if i == j:
            matrix[i].append(int(iaux + jaux))
        else:
            matrix[i].append(int(2 * iaux - 2 * jaux))
        if iaux == 2 and jaux == 2:
            a22 = matrix[i][j]
        if iaux == 3 and jaux == 4:
            a34 = matrix[i][j]

show(matrix)
print(f"A soma de a22 ({a22}) e a34 ({a34}) = {a22 + a34}")
