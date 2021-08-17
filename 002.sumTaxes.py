def somaImposto(taxaImposto, custo):
    return custo + (custo * taxaImposto / 100)


cost = float(input("Informe o valor do produto: R$ "))
tax = float(input("Informe a taxa de juros: "))

finalPrice = somaImposto(tax, cost)
print(f"O valor final do produto com as taxas é de R${finalPrice:.2f}")
