nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

Media= (nota1 + nota2 + nota3)/3

if Media >= 6:
    print("aprovado")
elif Media >= 5:
    print("conselho de classe")
else: 
        print("reprovado")
