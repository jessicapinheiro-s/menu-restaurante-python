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

somaLanche = 0
somaBebida = 0
somaSobremesa = 0

print('Olá', nome)
print('1 - LANCHE')
print('2 - BEBIDA')
print('3 - SOBREMESA')
print('4 - SOMAR CONTA')
print('5 - ENCERRAR')

opcao = int(input('Selecione a opção do menu'))    

while(opcao != 4):
    if opcao == 1:
        print('A opção 1 foi selecionada')
        print('1 - CACHORRO QUENTE', precoCach)
        print('2 - HAMBURGUER', precoHam)
        print('3 - MISTO QUENTE', precoMist)
        opcaoLanche = int(input('Selecione a opção do menu'))
        if opcaoLanche == 1:
            somaLanche += precoCach
        elif opcaoLanche == 2:
            somaLanche +=precoHam
        else:
            somaLanche +=precoMist   
        
    elif opcao == 2:
        print('A opção 2 foi selecionada')
        print('1 - COCA', precoCoca)
        print('2 - FANTA', precoFanta)
        print('3 - SUCO', precoSuco)
        opcaoBebida = int(input('Selecione a opção do menu'))
        if opcaoBebida == 1:
            somaBebida += precoCoca
        elif opcaoBebida == 2:
            somaBebida +=precoFanta
        else:
            somaBebida +=precoSuco   
        
    else:
        print('A opção 3 foi selecionada')
        print('1 - PUDIM', precoPudim)
        print('2 - BALA', precoBala)
        print('3 - PAVÊ', precoSuco)
        opcaoSobremesa = int(input('Selecione a opção do menu'))

        if opcaoSobremesa == 1:
            somaSobremesa += precoPudim
        elif opcaoSobremesa == 2:
            somaSobremesa +=precoBala
        else:
            somaSobremesa +=precoSuco  
    total = somaSobremesa + somaBebida + somaLanche
    print('O total da sua conta deu R$', total) 
    if opcao == 4:
        break


