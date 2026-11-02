import math

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores devem ser positivos.")

elif a + b > c and a + c > b and b + c > a:

    p = (a + b + c) / 2

    area = math.sqrt(
        p * (p - a) * (p - b) * (p - c)
    )

    print("Os valores formam um triângulo.")
    print(f"A área do triângulo é: {area:.2f}")

else:
    print("Os valores não formam um triângulo.")
    print(f"Valores informados: {a}, {b}, {c}")
