def aplicar_desconto(preco):
    if preco > 0:
        desconto = preco * 0.10
        preco_desconto = preco - desconto
        return preco_desconto

preco = float(input(print("Digite o preco:")))

valor = aplicar_desconto(preco)
print(f"valor com desconto:{valor}")