water_consumed = float(input("Água Consumida(L/dia): "))
if (water_consumed >= 0) and (water_consumed <= 200):
    if water_consumed < 150:
        print("Alta sustentabilidade")
    if 150 <= water_consumed <= 200:
        print("Moderada sustentabilidade")
else:
    print("Baixa sustentabilidade")