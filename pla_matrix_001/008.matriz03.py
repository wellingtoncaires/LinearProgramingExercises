from functions.createdFunctions import show
from functions.createdFunctions import sumMatrix
from functions.createdFunctions import multiplyMatrix
from functions.createdFunctions import subMatrix

print("Calcule as matrizes A+B-4*C, conforme as matrizes A, B e C passadas:")
print()
A = [[0, 3], [2, -5]]
print(f"{'Matriz A:':^18}")
show(A)
print()
B = [[-2, 4], [0, -1]]
print(f"{'Matriz B:':^18}")
show(B)
C = [[4, 2], [-6, 0]]
print(f"{'Matriz C:':^18}")
show(C)
auxMult = multiplyMatrix(C, 4)
print("Reultado 4 * C:")
show(auxMult)
auxSum = sumMatrix(A, B)
print(f"{'Reultado A+B:':^18}")
show(auxSum)
result = subMatrix(auxSum, auxMult)
print("Reultado A+B - 4 * C:")
show(result)
