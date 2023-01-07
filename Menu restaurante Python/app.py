nome = input('Qual é o seu nome?')

precoHam = 15.65
precoCach = 10.86
precoMist = 8.43


precoCoca = 6.00
precoFanta = 5.60
precoSuco = 5.00

precoBala = 0.50
precoPudim = 8.00
precoPave = 9.00


print('Olá', nome)
print('1 - LANCHE')
print('2 - BEBIDA')
print('3 - SOBREMESA')
opcao = int(input('Selecione a opção do menu'))
if opcao == 1:
    print('A opção 1 foi selecionada')
    print('1 - CACHORRO QUENTE', precoCach)
    print('2 - HAMBURGUER', precoHam)
    print('3 - MISTO QUENTE', precoMist)
    opcaoLanche = int(input('Selecione a opção do menu'))
elif opcao == 2:
    print('A opção 2 foi selecionada')
    print('1 - COCA', precoCoca)
    print('2 - FANTA', precoFanta)
    print('3 - SUCO', precoSuco)
    opcaoLanche = int(input('Selecione a opção do menu'))
else:
    print('A opção 2 foi selecionada')
    print('1 - PUDIM', precoCoca)
    print('2 - BALA', precoFanta)
    print('3 - PAVÊ', precoSuco)
    opcaoLanche = int(input('Selecione a opção do menu'))

