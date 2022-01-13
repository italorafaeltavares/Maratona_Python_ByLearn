# if(se) | Elif(senão se) | Else(senão)
#if == 'Rafael':
#if >= 23:




horario = 'dia'

if horario == 'dia':
    print('Está de dia')
elif horario == 'tarde':
    print("Está de tarde")
elif horario == 'noite':
    print("Está de noite")    
else:
    print("Está de madrugada")    


temperatura = 21

if temperatura <= 30:
    print("Hoje não está tão quente")
else :
    print("Hoje está quente")    


number = 8

if number == 1 or number == 3 or number == 5:
    print('Não permitido')
elif number == 2 or number == 4:
    print('Permitido')
else:
    print('Erro')    
        

# Laços de repetição
for numero in range(1,11):
    print(numero)




