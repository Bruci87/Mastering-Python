# Leia uma temperatura em graus Celsius e apresente o valor convertido para graus Fahrenheit.
# A fórmula de conversão é:
# F = (9 * C + 160) / 5
# Onde:
# F = temperatura em Fahrenheit
# C = temperatura em Celsius
C = float(input("Digite a temperatura em graus Celsius: "))
if(C < -273.15):
    F = (9 * C + 160) / 5
else:  
    F = (9 * C + 160) / 5
    print("A temperatura em graus Fahrenheit é: ", F)