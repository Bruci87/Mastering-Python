# Leia dois valores inteiros A e B e calcule: adição, subtração, multiplicação, divisão de A por B. Mostre todos os resultados.
# Em seguida, leia dois valores lógicos (True ou False) nas variáveis C e D, e realize as seguintes operações: negação de C e de D (not), conjunção (and), disjunção (or). Mostre os resultados das operações.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
ABMais = A + B
ABMenos = A - B
ABMultiplicacao = A * B
ABDivisao = A / B
print("Resultados das operações com A e B:")
print("A + B =", ABMais)    
print("A - B =", ABMenos)
print("A * B =", ABMultiplicacao)
print("A / B =", ABDivisao)
print("\nAgora, vamos trabalhar com os valores lógicos.")
C = input("Digite o valor de C (True ou False): ")
D = input("Digite o valor de D (True ou False): ")
CDNot = not (C == "True")
DCNot = not (D == "True")
CDAnd = (C == "True") and (D == "True")
DCAnd = (D == "True") and (C == "True")
CDOr = (C == "True") or (D == "True")
DCOr = (D == "True") or (C == "True")
print("Resultados das operações com C e D:")
print("not C =", CDNot)
print("not D =", DCNot)
print("C and D =", CDAnd)
print("D and C =", DCAnd)
print("C or D =", CDOr)
print("D or C =", DCOr)
