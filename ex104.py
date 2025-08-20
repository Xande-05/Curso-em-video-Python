def leiaint(número):
    num= (str(input(f'{número}')))
    if num == '':
        num = '0'
    if num.isalpha():
        while num.isalpha():
            num= (str(input('Por favor digite um número: ')))
    return num


n= leiaint('Digite um número: ')
print (f'Você acabou de digitar o número {n}')