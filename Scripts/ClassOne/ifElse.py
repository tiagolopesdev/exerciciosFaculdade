print("Escolha o codigo de compra abaixo:")
a = int(input("\n1 - 5222\n2 - 5333\n3 - 5444\n"))

if a == 1:
    print("Compra à vista")
elif a == 2:
    print("Compra à prazo no boleto")
elif a == 3:
    print("Compra à prazo no cartão")
else:
    print("Ops!! não cadastrado")