número = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    escolha = int (input ('Digite um número entre 0 e 20: '))
    while escolha not in range(0, 21):
        escolha = int(input('Opção inválida, digite um número entre 0 e 20: '))
    print (f'Você digitou o número {número[escolha]}.')
    desejo = input('Quer continuar? [S/N] ').upper()[0]
    if desejo in 'NnSs':
        if desejo in 'Nn':
            break
    else:
        desejo = input('Opão inválida, você deseja continuar? [S/N] ')
print ('Fim do programa.')