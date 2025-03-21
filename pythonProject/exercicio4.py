valorEmReal = float(input("Digite um valor em real: "))
dolar = float(input("Digite a cotação do dolar: "))

valorEmDolar = valorEmReal / dolar
print(f"O valor em dólar será: U${valorEmDolar:.2f}")