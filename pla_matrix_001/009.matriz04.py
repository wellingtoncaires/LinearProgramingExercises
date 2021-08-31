from functions.createdFunctions import show
from functions.createdFunctions import transposedtMatrix
from functions.createdFunctions import sumMatrix

print("Dada a Matriz A, obtenha a matriz B tal que B = A + At")
print()
A = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
print(f"{'Matriz A:':^22}")
show(A)

aT = transposedtMatrix(A)
print(f"{'Matriz At:':^22}")
show(aT)

B = sumMatrix(A, aT)
print(f"{'Matriz B:':^22}")
show(B)


