# Verificar  estado do dia
horario = 'dia'

if horario == 'dia':
    print('Está de dia')
elif horario == 'tarde':
    print("Está de tarde")
elif horario == 'noite':
    print("Está de noite")    
else:
    print("Está de madrugada")    

#Temperatura
temperatura = 21

if temperatura <= 30:
    print("Hoje não está tão quente")
else :
    print("Hoje está quente") 


# Para utlilizar o brinquedo deve possuir:
# Idade  >= 15 e altura >= 160 cm

idade = float(input('Informe sua idade: '))
altura = float(input('Informe sua Altura em cm: '))

if idade >= 15 and altura >= 160:
    print('Permitido usar o brinquedo') 
elif idade < 15 and altura < 160:
        print('Idade e altura não permitida')     
elif idade < 15:
        print('Idade não permitida')
elif altura < 160:
        print('Altura não permitida')

# Aceita números de 5 a 10    
numero = int(input('Digite um úmero: '))

if numero >= 5:
    if numero <= 10:
        print('Número', + numero, 'é aceito')
    else:
        print('Deve ser maior que 5 e menor que 10')        
else:
    print(f'Numero {numero} não aceito')        





