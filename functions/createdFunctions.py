def create(line, column):
    matriz = []
    for line in range(0, line):
        matriz.append([])
    return matriz


def magicBoard(numbers):
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
        print(f"Soma da {n + 1}° linha: {aux[n]}")
    for n in range(3, 6):
        print(f"Soma da {n - 2}° Coluna: {aux[n]}")
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


def cpfValidator(cpf):
    cpf = cpf.replace('.', "")
    cpf = cpf.replace("-", "")
    digit = cpf[9:]
    check = 0
    aux = 10
    for i in range(0, 9):
        check += int(cpf[i]) * aux
        aux -= 1
    check = check % 11
    if check < 2:
        check = 0
    else:
        check = 11 - check
    if check != int(digit[0]):
        return False
    aux = 11
    check = 0
    for i in range(0, 10):
        check += int(cpf[i]) * aux
        aux -= 1
    check = check % 11
    if check < 2:
        check = 0
    else:
        check = 11 - check
    if check != int(digit[1]):
        return False
    return True


def matrixCheck(a, b, signal="*"):
    if signal == "*":
        if len(a[0]) == len(b):
            return True
        else:
            return False
    elif signal == "+" or signal == "-":
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            return True
        else:
            return False


def transposedtMatrix(a):
    line = len(a)
    column = len(a[0])
    b = create(column, line)
    for i in range(0, line):
        for j in range(0, column):
            b[i].append(a[j][i])
    return b


def multiplyMatrix(a, b):
    line = len(a[0])
    column = len(a[0])
    ax1 = create(line, column)
    if type(b) == list:
        if matrixCheck(a, b, "*"):
            for i in range(0, line):
                c = 0
                while c < line:
                    aux = 0
                    for j in range(0, line):
                        aux += a[i][j] * b[j][c]
                    ax1[i].append(aux)
                    c += 1
            return ax1
        else:
            return None
    elif type(b) == float or type(b) == int:
        for i in range(0, line):
            for j in range(0, column):
                n = b * a[i][j]
                ax1[i].append(n)
        return ax1


def sumMatrix(a, b):
    if matrixCheck(a, b, "+"):
        line = len(a)
        auxSum = create(line, line)
        for i in range(0, line):
            for j in range(0, line):
                auxSum[i].append(a[i][j] + b[i][j])
        return auxSum
    else:
        return None


def subMatrix(a, b):
    if matrixCheck(a, b, "-"):
        line = len(a)
        auxSum = create(line, line)
        for i in range(0, line):
            for j in range(0, line):
                auxSum[i].append(a[i][j] - b[i][j])
        return auxSum
    else:
        return None


def show(a):
    line = len(a)
    column = len(a[0])
    for i in range(0, line):
        for j in range(0, column):
            print(f"{round(a[i][j], 2):5}", end=" ")
        print()
    print()


def identityMatrix(a):
    lines = len(a)
    columns = len(a[0])
    b = create(lines, columns)
    for i in range(0, lines):
        for j in range(0, columns):
            if i == j:
                b[i].append(1)
            else:
                b[i].append(0)
    return b


def inverseSquared(a):
    lines = len(a)
    inverse = a
    mainDiagonal = 1
    secondaryDiagonal = 1
    for i in range(0, lines):
        for j in range(0, lines):
            if i == j:
                mainDiagonal *= a[i][j]
            else:
                secondaryDiagonal *= a[i][j]
    det = mainDiagonal - secondaryDiagonal
    for i in range(0, lines):
        for j in range(0, lines):
            a[i][j] = a[i][j] / det
    first = a[0][0]
    for i in range(0, lines):
        for j in range(0, lines):
            if i == j:
                if i == 0:
                    inverse[i][j] = a[i + 1][j + 1]
                else:
                    inverse[i][j] = first
            else:
                inverse[i][j] = -1 * a[i][j]
    return inverse
