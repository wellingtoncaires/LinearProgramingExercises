from createdFunctions import create

print("Calcule as matrizes A+B-4*C, conforme as matrizes A, B e C passadas:")
A = [[0, 3], [2, -5]]
print("Matriz A:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{A[i][j]:3}", end=" ")
    print()
print()
B = [[-2, 4], [0, -1]]
print("Matriz B:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{B[i][j]:3}", end=" ")
    print()
print()
C = [[4, 2], [-6, 0]]
print("Matriz C:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{C[i][j]:3}", end=" ")
    print()
auxSum = create(2, 2)
for i in range(0, 2):
    for j in range(0, 2):
        auxSum[i].append(A[i][j] + B[i][j])
print()
print("Reultado A+B:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{auxSum[i][j]:3}", end=" ")
    print()
auxMult = create(2, 2)
for i in range(0, 2):
    for j in range(0, 2):
        auxMult[i].append(4 * C[i][j])
print()
print("Reultado 4*C:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{auxMult[i][j]:3}", end=" ")
    print()
result = create(2, 2)
for i in range(0, 2):
    for j in range(0, 2):
        result[i].append(auxSum[i][j] - auxMult[i][j])
print()
print("Reultado A+B - 4*C:")
for i in range(0, 2):
    for j in range(0, 2):
        print(f"{result[i][j]:3}", end=" ")
    print()


