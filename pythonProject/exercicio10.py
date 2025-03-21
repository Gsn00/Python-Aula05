diasTrabalhados = int(input("Digite a quantidade de dias de trabalho: "))
valorFinal = (diasTrabalhados * 80)
valorFinal -= valorFinal * .08
print(f"O salário desse trabalhador será R${valorFinal:.2f}")