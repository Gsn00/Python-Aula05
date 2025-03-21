segundosTotais = int(input("Digite a quantidade de segundos: "))

hh = segundosTotais // 60 // 60
mm = segundosTotais // 60 - (hh * 60)
ss = segundosTotais % 60 % 60

print(f"Horas: {hh} horas {mm} minutos e {ss} segundos")

