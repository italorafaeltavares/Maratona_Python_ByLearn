# Meu primeiro Projeto - Calculado Top
print("Bem Vindo a ByCalculator 2000")

firstNumber  = float(input("Digite o primeiro número: "))
secondNumber = float(input("Digite o segundo número: "))

addition = firstNumber + secondNumber
subtraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber / secondNumber

restDivision =  firstNumber % secondNumber
divisioEnteri = firstNumber // secondNumber

firstSquare = firstNumber ** 2
seconndCube = secondNumber ** 3

print (f"{firstNumber} + {secondNumber} = {addition}")
print (f"{firstNumber} - {secondNumber} = {subtraction}")
print (f"{firstNumber} * {secondNumber} = {multiplication}")
print (f"{firstNumber} / {secondNumber} = {division}")
print (f"O resto da divisão de {firstNumber} por {secondNumber} = {restDivision}")
print (f"A divisão inteira de {firstNumber} por {secondNumber} = {divisioEnteri}")
print (f"{firstNumber} ao quadrado é = {firstSquare}")
print (f"{secondNumber} ao cubo é = {seconndCube}")
print("Obrigado por utilizar a ByCalculator 2000")

