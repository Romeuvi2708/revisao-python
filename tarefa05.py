def calcular_imc(peso, altura):
    imc = peso / (altura **2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    else:
        return "Acima do peso"
    
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(peso, altura)
print("Seu imc é:", round(imc, 2))

classificacao = classificar_imc(imc)
print(f"Classificação: {classificacao} ")