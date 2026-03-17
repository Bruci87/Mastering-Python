# Leia o custo de fábrica de um carro e mostre o custo final ao consumidor.
cF = float(input("Qual o preço de fábrica do carro? "))
cF = cF + (cF * 0.28) + (cF * 0.45)
print("O preço final do carro é: R$%.2f" % cF)