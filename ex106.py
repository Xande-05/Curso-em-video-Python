from time import sleep
def ajuda(com):
    help(com)
    print ('-'*30)
    print (f'Acessando o manual do comando {comando}...')
    print ('-'*30)
    sleep(1)

    
comando=''
while True:
    print ('-'*30)
    print ('    SISTEMA DE AJUDA PyHELP')
    print ('-'*30)
    comando= (str(input('função ou biblioteca: '))).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)

print ('Fim do programa')