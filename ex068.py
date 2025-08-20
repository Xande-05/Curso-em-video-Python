from random import randint
contador = 0
while True:
    computador = randint(1, 10)
    print ('Vamos jogar par ou ímpar!')
    escolha = str(input('Par ou ímpar? [P/I]: ')).strip().upper()
    while escolha not in 'PI':
        escolha = str(input('Opção inválida, escolhe par ou ímpar? [P/I]: ')).strip().upper()
    jogador = int(input('Digite um valor: '))
    resultado = computador + jogador
    if escolha == 'P':
        if resultado % 2 == 0:
            print (f'O resultado de {jogador} mais {computador} foi par e você venceu!')
        else:
            print (f'O resultado de {jogador} mais {computador} foi ímpar e você perdeu!')
            break
    elif escolha == 'I':
        if resultado % 2 == 1:
            print (f'O resultado de {jogador} mais {computador} foi ímpar e você venceu!')
        else:
            print (f'O resultado de {jogador}  mais {computador} foi par e você perdeu!')
            break
    contador += 1
print ('Fim de jogo.')
print (f'Você ganhou {contador} vezes.')