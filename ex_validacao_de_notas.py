n1: float; n2: float; media: float

n1 = int(input("Digite a primeira nota: "))
if n1 < 0 or n1 > 10:
        print("Nota invalida. Digite novamente:")
        n1 = int(input("Digite a primeira nota: "))

n2 = int(input("Digite a segunda nota: "))
if n2 < 0 or n2 > 10:
        print("Nota invalida. Digite novamente:")
        n2 = int(input("Digite a segunda nota: "))

media = n1 + n2 / 2
print(f"A média é de: {media:.2f}")
