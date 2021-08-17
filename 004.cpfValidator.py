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


cpf = str(input("Digite seu CPF (XXX.XXX.XXX-XX): "))
valid = cpfValidator(cpf)

if valid:
    print(f"CPF {cpf} é válido!")
else:
    print(f"CPF {cpf} não é um número válido!")

# 529.982.247-25
# 111.444.777-35
# 145.382.206-20

# Inválidos
# 111.222.333-45
