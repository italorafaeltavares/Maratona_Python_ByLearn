# Verificar dias da semana
dia = input('Informe o dia: ')

if dia == 'sabado' or  dia == 'domingo':
    print(f"Hoje é {dia} estamos no final de semana")
elif dia == 'segunda' or dia == 'terca' or dia == 'quarta' or dia == 'quinta': 
    print(f"Hoje é {dia} estamos na semana")
elif dia == 'sexta':
    print('Sextou !!!')     
else :
    print('Dia digitado não é valido')  