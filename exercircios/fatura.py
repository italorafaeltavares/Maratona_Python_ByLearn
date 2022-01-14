# Veririca se o saldo da fatura está no valor apropiado.
valor_diponivel_mes =float(input('Informe o valor disponivel para pagamento de fatura: '))
valor_fatura = float(input('Informe o valor cobrado da fatura: '))

if valor_fatura < valor_diponivel_mes:
    print(f'Para este valor de {valor_fatura:.2f} não e necessário realizar empréstimo')
elif valor_fatura == valor_diponivel_mes:
    print(f'O valor de {valor_fatura:.2f} já está consideravel, manere nos gastos')    
else:
    print(f'Para esta valor de {valor_fatura:.2f} você precisara realizar empréstimo')
