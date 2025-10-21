try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado} ")

except ValueError:
    print("Erro: número inváilido!")

except ZeroDivisionError:
    print("ERRO: não é possivel dividir por zero!")