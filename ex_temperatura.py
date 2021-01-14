cels: float; fahr: float

escala = str(input("Voce vai digitar a temperatura em qual escala (C/F)? "))

if escala == 'F':
	fahr = float(input("Digite a temperatura em Fahrenheit: "))

	cels = 5.0 / 9.0 * (fahr - 32.0)
	print(f"Temperatura equivalente em Celsius: {cels:.2f}")
else:
	cels = float(input("Digite a temperatura em Celsius: "))

	fahr = cels * 9.0 / 5.0 + 32.0;
	print(f"Temperatura equivalente em Fahrenheit: {fahr:.2f}")