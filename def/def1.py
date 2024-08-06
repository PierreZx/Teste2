
def liner_q(coeficiente_a,coeficiente_b):
    coeficiente_a = float(input("Digite o coeficiente 'a': "))
    coeficiente_b = float(input("Digite o coeficiente 'b': "))
    if coeficiente_a == 0:
        if coeficiente_b == 0:
            print("A equação é indeterminada (infinitas soluções).")
        else:
            print("A equação é impossível (não há solução).")
    else:
        x = -coeficiente_b / coeficiente_a
    return x
coeficiente_a = float(input("Digite o coeficiente 'a': "))
coeficiente_b = float(input("Digite o coeficiente 'b': "))

solucao = liner_q(coeficiente_a, coeficiente_b)

if solucao is not None:
    print("A solução da equação é x =", solucao)