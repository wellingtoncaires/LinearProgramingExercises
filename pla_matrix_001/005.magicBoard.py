from functions.createdFunctions import magicBoard
from functions.createdFunctions import create


matrix = create(3, 3)
for i in range(0, 3):
    for j in range(0, 3):
        matrix[i].append(int(input(f"Digite o número [{i}, {j}]: ")))

magicBoard(matrix)
