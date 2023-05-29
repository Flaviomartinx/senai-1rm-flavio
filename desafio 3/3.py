salario = float(input("Digite o salário do funcionário: "))

if salario > 8250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print("O novo salário é: R$", novo_salario)