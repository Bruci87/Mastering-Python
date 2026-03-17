valorCompra = float(input("Digite o preço da sua compra"))
parcelar = str(input("Deseja parcdelar?"))
if(parcelar == "sim"):
    qntdParcelas = int(input("quantas vezes deseja parcelar? Em ate 10 vezes"))
    total =valorCompra / qntdParcelas
    print("Valor total a pagar: R$", total)
else:
    print("Valor total a pagar: R$", valorCompra)
