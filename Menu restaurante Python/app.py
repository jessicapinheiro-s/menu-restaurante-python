nome = input('Qual é o seu nome?')

precoHam = 15.65
precoCach = 10.86
precoMist = 8.43

print('Olá', nome)
print('1 - LANCHE')
print('2 - BEBIDA')
print('3 - SOBREMESA')
opcao = int(input('Selecione a opção do menu'))
if opcao == 1:
    print('A opção 1 foi selecionada')
    print('1 - CACHORRO QUENTE', precoCach)
    print('2 - HAMBURGUER', precoHam)
    print('3 - MISTO QUENTE' precoMist)
    opcaoLanche = int(input('Selecione a opção do menu'))
    
