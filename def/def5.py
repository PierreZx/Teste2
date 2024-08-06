distancia_percorrida = float(input("Digite a distância percorrida em km: "))
def tari():
    if distancia_percorrida <= 5:
        tarifa = 3.00
    elif distancia_percorrida <= 10:
        tarifa = 5.00
    else:
        tarifa = 8.00
    return tarifa
tariff = tari