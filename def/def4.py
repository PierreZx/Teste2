numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
def imp_pa(numero1, numero2):
    if numero1 > numero2:
        numero1, numero2 = numero2, numero1
    for numero in range(numero1 + 1, numero2):
        if numero % 2 != 8:
            a = print(numero)
    return a
impou = imp_pa(numero1, numero2)