numero = int(input("Digite um número inteiro: "))

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print("O fatorial de", numero, "é", fatorial)