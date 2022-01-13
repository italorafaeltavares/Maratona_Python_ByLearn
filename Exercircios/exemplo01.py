#Acerta 8 como número digitado
numero = int(input('Digite um numero inteiro: '))

if numero == 8:
    print('Você acertou o número ')
elif numero < 8:
    print('Você errou !!! digitou um número menor')    
else :
    print('Você errou !!! digitou um número maior')    

# Verificar dias da semana
dia = input('Informw o dia: ')

if dia == 'sabado' or  dia == 'domingo':
    print(f"Hoje é {dia} estamos no final de semana")
elif dia == 'segunda' or dia == 'terca' or dia == 'quarta' or dia == 'quinta': 
    print(f"Hoje é {dia} estamos na semana")
elif dia == 'sexta':
    print('Sextou !!!')     
else :
    print('Dia digitado não é valido')     