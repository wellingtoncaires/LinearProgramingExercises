from createdFunctions import transposedtMatrix
from createdFunctions import create
from createdFunctions import show
from createdFunctions import multiplyMatrix
from createdFunctions import inverseSquared
from createdFunctions import sumMatrix
from createdFunctions import subMatrix

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
aT = transposedtMatrix(a)
cI = inverseSquared(c)
bT = transposedtMatrix(b)
result = create(2, 2)

print(f"{'Matriz B + At:':^18}")
result = sumMatrix(b, aT)
show(result)
print(f"{'Resultado 1 * Ci:'}")
aux = multiplyMatrix(result, cI)
show(aux)
print(f"{'Resultado 3 * Bt:'}")
result = multiplyMatrix(bT, 3)
show(result)
print(f"{'Resultado Final:'}")
final = subMatrix(aux, result)
show(final)
