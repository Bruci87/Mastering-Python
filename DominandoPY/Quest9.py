# Converta um valor em dólares (US$) para reais (R$).
#  O programa deve ler:
# o valor da cotação do dólar
# a quantidade de dólares que o usuário deseja converter
ctDollar = float(input("Digite a cotação do dólar: "))
qtndDollar = float(input("Digite a quantidade de dólares que deseja converter: "))
real = qtndDollar / ctDollar
print(f"O valor convertido em reais é: R$ ", real)