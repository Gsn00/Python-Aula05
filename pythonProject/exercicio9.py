total = 780000
primeiroValor = total * .46
segundoValor = total * .32
terceiroValor = total - primeiroValor - segundoValor

print(f"Prêmios: \n 1° lugar - R${primeiroValor:.2f}"
      f"\n 2° lugar - R${segundoValor:.2f}"
      f"\n 3° lugar - R${terceiroValor:.2f}")