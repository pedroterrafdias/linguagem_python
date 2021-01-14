nota1: float; nota2: float; media: float

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = nota1 + nota2 / 2

if media < 6 :
    print("Você está reprovado")
    print(f"A sua média é de: {media:.2f}")
else:
    print("Você está aprovado")
    print(f"A sua média é de: {media:.2f}")