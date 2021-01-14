min: float
valor: int

min = float(input("Digite a quantidade de minutos falados: "))

if min < 100:
    print(f"O valor a pagar é: 50")
else:
    valor = 50 + ((min - 100) * 2)
    print(f"O valor a pagar é de: {valor}")