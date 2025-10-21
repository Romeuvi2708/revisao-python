try:
    numero = float(input("Digite um numero: "))
    print(f"Você digitou: {numero}")

except ValueError:
    print("Erro: você deve digitar um número válido! ")