def dividir(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        return "Erro: não existir divisão por zero!"
    
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado = dividir(numero1, numero2)
print(f"Resultado: {resultado}")

