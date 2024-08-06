preco_produto1= float(input("Digite o preço do produto 1: "))
preco_produto2= float(input("Digite o preço do produto 2: "))
preco_produto3 = float(input("Digite o preço do produto 3: "))
def prec(preco_produto1, preco_produto2, preco_produto3):
    mais_barato= preco_produto1

    if preco_produto2 < mais_barato:
        mais_barato = preco_produto2
    if preco_produto3 < mais_barato:
        mais_barato = preco_produto3
    return print('Voce deve comprar o produto de preço: ', mais_barato)
preco = prec(preco_produto1, preco_produto2, preco_produto3)
