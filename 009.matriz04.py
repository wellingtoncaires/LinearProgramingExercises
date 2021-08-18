from createdFunctions import create

print("Dada a Matriz A, obtenha a matriz B al que B = A + At")
A = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
print("Matriz A:")
for i in range(0, 3):
    for j in range(0, 3):
        print(f"{A[i][j]:3}", end=" ")
    print()

aT = create(3, 3)
for i in range(0, 3):
    for j in range(0, 3):
        aT[i].append(int(A[j][i]))
print()
print("Matriz At:")
for i in range(0, 3):
    for j in range(0, 3):
        print(f"{aT[i][j]:3}", end=" ")
    print()

B = create(3, 3)
for i in range(0, 3):
    for j in range(0, 3):
        B[i].append(int(A[i][j] + aT[i][j]))
print()
print("Matriz B:")
for i in range(0, 3):
    for j in range(0, 3):
        print(f"{B[i][j]:3}", end=" ")
    print()
