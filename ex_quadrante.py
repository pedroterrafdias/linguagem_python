x: int; y: int

print("Digite os valores das coordenadas X e Y:")
x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("Está no primeiro quadrante.")
    elif x > 0 and y < 0:
        print("Está no segundo quadrante.")
    elif x < 0 and y < 0:
        print("Está no terceiro quadrante.")
    else:
        print("Está no quarto quadrante.")

    print("Digite os valores das coordenadas X e Y:")
    x = int(input())
    y = int(input())