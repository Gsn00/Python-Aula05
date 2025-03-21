votosBrancos = int(input("Quantidade de votos em branco: "))
votosNulos = int(input("Quantidade de votos nulos: "))
votosValidos = int(input("Quantidade de votos válidos: "))

total = votosValidos + votosNulos + votosBrancos
votosBrancosPercent = 100 * votosBrancos / total
votosNulosPerent = 100 * votosNulos / total
votosValidosPercent = 100 * votosValidos / total

print(f"Percentual:\n - Votos em branco: {votosBrancosPercent:.2f}%"
      f"\n - Votos em branco: {votosNulosPerent:.2f}%"
      f"\n - Votos em branco: {votosValidosPercent:.2f}%")
