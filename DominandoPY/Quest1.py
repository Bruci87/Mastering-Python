# Leia a idade de uma pessoa expressa em anos, meses e dias e mostre essa idade expressa apenas em dias.
ano = int(input("digite o ano"))
mes = int(input("digite o mes"))
dia = int(input("digite o dia"))
print("Sua idade: ", ano *365 + mes * 3 + dia, "Dias" )