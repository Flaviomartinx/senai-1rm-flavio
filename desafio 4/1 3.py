numero = int(input("Digite um número: "))

print("Tabuada de", numero)
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)