from createdFunctions import cpfValidator


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
