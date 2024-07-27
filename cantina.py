# bem vindo!
print("Olá, seja bem-vindo(a) à Ronalda Lanches! Siga os passos a seguir para efetuar seu pedido: ")


# área de customização dos preços:
dicBebidas = {"cafe": 2.50, "suco": 3.50, "refrigerante": 4.05}
precoCafe = dicBebidas["cafe"]
precoSuco = dicBebidas["suco"]
precoRefri = dicBebidas["refrigerante"]
produtoCliente = []

# inputs:
while True:
    novo_produto = str(input("Digite uma bebida para adicionar ao carrinho e \
digite ´sair´ para finalizar seu pedido: ")).lower().strip()
    if novo_produto == "cafe" or novo_produto == "suco" or novo_produto == "refri" or novo_produto == "refrigerante"\
            or novo_produto == "café" or novo_produto == "cafes" or novo_produto == "cafés" or novo_produto == "sucos":
        produtoCliente.append(novo_produto)

    if novo_produto == "sair":
        break

# contagem de produto:
qtdCafe = produtoCliente.count("café") or produtoCliente.count("cafe") or \
produtoCliente.count("cafes") or produtoCliente.count("cafés")
qtdSuco = produtoCliente.count("suco") or produtoCliente.count("sucos")
qtdRefri = produtoCliente.count("refrigerante") or produtoCliente.count("refri")

# preço final:
valorTotal = (qtdCafe * precoCafe) + (qtdSuco * precoSuco) + (qtdRefri * precoRefri)

# output para usuário:
if qtdSuco > 0:
    print(f"Na compra de {qtdCafe} café(s), {qtdSuco} suco(s) e {qtdRefri} refrigerantes, \
o valor total a ser pago será: {valorTotal:.2f}, mas, ao comprar um ou mais sucos, você irá ganhar 01 bolo de brinde! :)")
else:
    print(f"Na compra de {qtdCafe} café(s), {qtdSuco} suco(s) e {qtdRefri} refrigerantes, \
o valor total a ser pago será: R$: {valorTotal:.2f}.")
