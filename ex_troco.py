preco: float; troco: float; dinheiro: float
n: int

preco = float(input("Preço unitário do produto: "))
n = int(input("Quantidade: "))
dinheiro = float(input("Valor pago: "))

troco = dinheiro - (n * preco)
print(f"O troco é de: {troco:.2f}")