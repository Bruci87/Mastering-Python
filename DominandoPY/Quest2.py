
# Calcule e mostre a quantidade de dinheiro gasta por um fumante, lendo as seguintes informações:
# número de anos que ele fuma
# número de cigarros fumados por dia
# preço de uma carteira de cigarros

anosFumado = int(input("Quantos anos ja fuma?"))
QntdCigarrosDia = int(input("Quantoscigarro fuma por dia?"))
PrecoCigarro = float(input("Preco do cigarro?"))
anosFumado = anosFumado * 365
total =  anosFumado * QntdCigarrosDia
total = total * PrecoCigarro

print("O valor gasto com cigarros é: R$", total)