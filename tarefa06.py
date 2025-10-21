def imposto_preco(preco):
    imposto = preco * 0.15
    valor_final = preco + imposto
    return valor_final

preco = float(input("Digite o preço do produto: "))
valor_imposto = imposto_preco(preco)
print(f"Valor final com imposto:{round(valor_imposto, 2)} ")