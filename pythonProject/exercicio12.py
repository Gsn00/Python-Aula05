comprimento = float(input("Digite o comprimento em metros: "))
largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))

areaParedes = (comprimento * altura * 2) + (largura * altura * 2)
azulejos = areaParedes // 1.5

print(f"A quantidade total de azulejos será {azulejos}")