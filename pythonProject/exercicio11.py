paes = int(input("Quantidade de pães: "))
broas = int(input("Quantidade de broas: "))

valorTotal = paes * .38 + broas * 4.5
poupanca = valorTotal * .1

print(f"O valor total arrecadado no dia foi de R${valorTotal:.2f}\n"
      f"O valor a ser depositado na poupança será de R${poupanca:.2f}")