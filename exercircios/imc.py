#Calculo do IMC: Peso(kg) & Altura(cm)
peso = 86.5
altura = 1.75
#imc =  peso // (altura ** 2)
#print(imc)

seu_peso    = float(input("Digite o seu peso: "))
sua_altura  = float(input("Digite a sua altura: "))
imc =  seu_peso / (sua_altura ** 2)
# :.2f Definie casas descimais neste exmplo 2
print(f"Meu IMC é: {imc:.2f}")





