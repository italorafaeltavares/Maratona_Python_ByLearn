contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3

# Enquanto não digitar Fulano, eu vou pedir o nome novamente
nome = input("Digite seu nome: ") 

while nome != "Fulano":
  print("Você não é o Fulano!")
  nome = input("Digite seu nome: ")

print("Olá Fulano")


contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2