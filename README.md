##  <img align="center" alt="Python" height="30" width="40" src="https://www.vectorlogo.zone/logos/python/python-icon.svg"/> *PYTHON*

Aprendendo Python com a ByLearn (Maratona Python Faixa Preta) 



> Identação
```
Escopo Pai
     Escopo filho
         Escopo neto  
```
> Variaveis 
- int   ==> Inteiro (São números inteiros)
- str   ==> String  (São textos, sepre dentro de aspas)
- float ==> Decimais (Números com "virgula"/usar o ponto)
- bool  ==> Booleano (True ou False)

> Output
````
print("Hello World")
print(f"Meu IMC é: {imc:.2f}")
````
> Input
````
input("Digite o dado: ")
seuDado = float(input("Digite o dado: "))
````
> Condicionais: 
## if (se) | elif (senão se) | else (senão)
```` 
if == 'Rafael':
if >= 23:

temperatura = 21

if temperatura <= 30:
    print("Hoje não está tão quente")
else :
    print("Hoje está quente")  
````

- Igual  ==
- Diferente de  !=
- Menor  <
- Maior  >
- Menor ou Igual  <=
- Maior ou Igual  >=

> Operadores Lógicos  

- "E" => and (isso e aquilo)
- "OU" => or (isso ou aquilo)

> Laços de Repetição

Forma de evitar repetição de código permitindo executar o mesmo código várias e várias vezes.

- for

### Sintaxe
````
for variavel in intervalo/sequencia:

for numero in range(1,11):
    print(numero)

for contador in range(1,11,3):
    print(contador) 
````

- while : Conjunto de instruções será executado enquanto uma condição é atendida

### Sintaxe
````
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3
````






