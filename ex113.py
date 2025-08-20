def leiaint(inteiro):
    while True:
        try:
            num= (int(input(inteiro)))
        except(ValueError, TypeError):
            print ('ERRO. Por favor digite um número inteiro valido. ')
            continue
        except(KeyboardInterrupt):
            print ('Entrada de dados interrrompida pelo usuário.')
            return 0
        else:
            return num


def leiafloat(inteiro):
    while True:
        try:
            num= (float(input(inteiro)))
        except(ValueError, TypeError):
            print ('ERRO. Por favor digite um número inteiro valido. ')
            continue
        except(KeyboardInterrupt):
            print ('Entrada de dados interrrompida pelo usuário.')
            return 0
        else:
            return num


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro "{n1}" e o número real "{n2}".')
print ('Fim do programa.')
