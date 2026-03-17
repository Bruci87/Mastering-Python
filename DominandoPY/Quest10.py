# Leia dois valores inteiros nas variáveis val1 e val2, troque seus conteúdos e mostre o resultado.
# Exemplo: Se val1 = 10 e val2 = 11 Após a troca deve resultar:
# val1 = 11
# val2 = 10
val1 = int(input("Digite o valor de val1: "))
val2 = int(input("Digite o valor de val2: "))
aux = val1
val1 = val2
val2 = aux
print("Após a troca:")
print("val1 =", val1)
print("val2 =", val2)
