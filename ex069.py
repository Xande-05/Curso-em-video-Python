maiores = homens = mulheres = 0
while True:
    print ('CADASTRE UNA PERSONA')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    while sexo not in 'MF':
        sexo = str(input('Opção inválida, digite o sexo: [M/F]: ')).upper()
    desejo = str(input('Deseja continuar? [S/N]: ')).upper()
    while desejo not in 'SN':
        desejo = str(input('Opção inválida, deseja continuar? [S/N]: ')).upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if desejo == 'N':
        break
print (f'A - temos {maiores} pessoas maiores de idade.')
print (f'B - temos {homens} homens que foram cadastrados.')
print (f'C - temos {mulheres} mulheres com menos de 20 anos.')
print ('Fim do programa!')
