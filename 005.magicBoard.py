from createdFunctions import magigBoard
from createdFunctions import create



# array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(0, 3):
#     for j in range(0, 3):
#         array[i][j] = int(input(f"Digite o número [{i}, {j}]: "))
matriz = create(3, 3)
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite o número [{i}, {j}]: ")))

magigBoard(matriz)
