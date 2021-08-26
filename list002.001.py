from createdFunctions import transposedtMatrix
from createdFunctions import sumMatrix
from createdFunctions import show
from createdFunctions import subMatrix
from createdFunctions import multiplyMatrix

print("Dadas as matrizes A, B e C, clacule (B+At) * Ci - (3 * Bt)")
print()
a = [[2, 1], [-3, 4]]
b = [[0, -1], [2, 5]]
c = [[3, 0], [6, 1]]
print(f"{'Matriz A:':^18}")
show(a)
print(f"{'Matriz B:':^18}")
show(b)
print(f"{'Matriz C:':^18}")
show(c)

cT = transposedtMatrix(c)
print("Resultado 1 (B - Ct))")
aux = subMatrix(b, cT)
show(aux)
print("Resultado 2 (A + (B - Ct))")
aux2 = sumMatrix(a, aux)
show(aux2)
print("Resultado Final")
result = multiplyMatrix(aux2, b)
show(result)
