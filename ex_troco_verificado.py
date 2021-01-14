valor: float; troco: float; dinheiro: float
n: int

valor = float(input("Digite o valor da mercadora: "))
n = int(input("Digite a quantidade do produto: "))
dinheiro = float(input("Digite o dinheiro entregue: "))

troco = dinheiro - (valor * n)
print(f"O troco é de: {troco:.2f}")

if (valor * n) > dinheiro:
    print("Dinheiro insuficiente")