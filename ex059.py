opcao = 5
while opcao == 5:
    opcao = 1
    print('------------------------------------------------')
    n1= int (input ('Digite aqui o primeiro número: '))
    n2= int (input ('Digiye aqui o segundo número: '))
    while opcao != 6 and opcao != 5:
        print('------------------------------------------------')
        print ('Temos todas essas opções:')
        print ('[1] SOMA')
        print ('[2] MULTIPLICAÇÃO')
        print ('[3] MAIOR')
        print ('[4] MENOR')
        print ('[5] NOVOS NÚMEROS')
        print ('[6] SAIR')
        opcao= int (input ('Escolha uma opção acima: '))
        if opcao == 1:
            print ('A soma entre {} e {} é igual a: {}'.format(n1,n2,n1+n2))
        elif opcao == 2:
            print ('A multiplicação entre {} e {} é igual a: {}'.format(n1,n2,n1*n2))
        elif opcao == 3:
            if n1 > n2:
                print ('O primeiro número é o maior')
            elif n1 < n2:
                print ('O segundo número é o maior')
            else:
                print ('Ambos são iguais.')
        elif opcao == 4:
            if n1 > n2:
                print ('O segundo número é o menor')
            elif n1 < n2:
                print ('O primeiro número é o maior')
            else:
                print ('Ambos são iguais.')
        elif opcao == 6:
            print ('Finalizando...')
        else:
            print ('Opção inválida. Tente novamente.')
print ('Fim do programa!')
