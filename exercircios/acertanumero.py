import random

numero_magico = random.randint(1,10)

print('Eu dúvido você acertar o número mágico')

numero_escolhido = int(input('Digite um número: '))

while numero_escolhido != numero_magico:
    print('Errou !!! tente novamente')

    if numero_escolhido > numero_magico:
        print('O número mágico é menor')
    elif numero_escolhido < numero_magico:        
        print('O número mágico é maior')

    numero_escolhido = int(input('Digite um número: '))   

print(f'Acertou !!! o número mágico é {numero_magico}')

# Acerta 8 como número digitado
# numero = int(input('Digite um numero inteiro: '))

# if numero == 8:
#     print('Você acertou o número ')
# elif numero < 8:
#     print('Você errou !!! digitou um número menor')    
# else :
#     print('Você errou !!! digitou um número maior')    


