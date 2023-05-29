def area(largura, comprimento):
    return largura * comprimento

largura = float(input("largura do terreno: "))
comprimento = float(input("comprimento do terreno: "))

area_terreno = area(largura, comprimento)

print("A área do terreno é:", area_terreno "m2")