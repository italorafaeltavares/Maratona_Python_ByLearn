# Meu primeiro Projeto - Calculado Top
print("Bem Vindo a ByCalculator 2000")

first_number  = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo número: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

rest_division =  first_number % second_number
divisio_enteri = first_number // second_number

first_square = first_number ** 2
seconnd_cube = second_number ** 3

print (f"{first_number} + {second_number} = {addition}")
print (f"{first_number} - {second_number} = {subtraction}")
print (f"{first_number} * {second_number} = {multiplication}")
print (f"{first_number} / {second_number} = {division}")
print (f"O resto da divisão de {first_number} por {second_number} = {rest_division}")
print (f"A divisão inteira de {first_number} por {second_number} = {divisio_enteri}")
print (f"{first_number} ao quadrado é = {first_square}")
print (f"{second_number} ao cubo é = {seconnd_cube}")
print("Obrigado por utilizar a ByCalculator 2000")

