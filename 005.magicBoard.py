def magigBoard(numbers):
    aux = [0] * 8
    jump = 2
    for i in range(0, 3):
        for j in range(0, 3):
            print(numbers[i][j], end="   ")
            if i == 0:
                aux[0] += numbers[i][j]
            if i == 1:
                aux[1] += numbers[i][j]
            if i == 2:
                aux[2] += numbers[i][j]
            if j == 0:
                aux[3] += numbers[i][j]
            if j == 1:
                aux[4] += numbers[i][j]
            if j == 2:
                aux[5] += numbers[i][j]
            if i == j:
                aux[6] += numbers[i][j]
            if j == jump:
                aux[7] += numbers[i][j]
                jump -= 1
        print()
    for n in range(0, 3):
        print(f"Soma da {n+1}° linha: {aux[n]}")
    for n in range(3, 6):
        print(f"Soma da {n-2}° Coluna: {aux[n]}")
    print(f"Soma da diagonal principal: {aux[6]}")
    print(f"Soma da diagonal secundaria: {aux[7]}")
    control = aux[0]
    status = True
    for n in aux:
        if n != control:
            status = False
    print()
    if status:
        print("Os números informados formam um quadrado mágico!")
    else:
        print("Os números informados NÃO formam um quadrado mágico!")


# array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for i in range(0, 3):
#     for j in range(0, 3):
#         array[i][j] = int(input(f"Digite o número [{i}, {j}]: "))
#
# magigBoard(array)
teste = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
teste2 = [[2, 3, 1], [5, 8, 2], [7, 8, 8]]
magigBoard(teste)
