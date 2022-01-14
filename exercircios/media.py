print('Bem vindo, Verificar aprovação!')
# função para calcular media
def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return  media    
# função para verificar aprovação 
def verifica_aprovacao(media):
    if media >= 7:
        print('Parabéns aprovado')
    elif media >= 5 and media <= 6:
        print('Recuperação')        
    else:
        print('Reprovado') 

# input dos dados das notas
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

# Chamada das funções
media_aluno = calcular_media(nota1, nota2)
verifica_aprovacao(media_aluno)


