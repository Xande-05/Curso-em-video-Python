from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio > fim:
        contador = inicio
        while contador >= fim:
            print (contador, end=' ')
            sleep(0.5)
            contador -= passo
        print ('\nFim da contagem.')
    else:
        contador = inicio
        while contador <= fim:
            print (contador, end=' ')
            sleep(0.5)
            contador += passo
        print('\nFim da contagem.')


print ('=-'*30)
print ('Contagem de 1 até 10 de 1 em 1')
sleep(1)
contador(1, 10, 1)

print ('=-'*30)
print ('Contagem de 10 até 0 de 2 em 2')
sleep(1)
contador(10, 0, 2)

print ('=-'*30)
print('Vamos agora fazer uma contagem personalizada!')
começo= (int(input('Digite o início da cntagem: ')))
final= (int(input('Digite o fim da contagem: ')))
pulo= (int(input('Digite o passo da contagem: ')))
contador(começo, final, pulo)
print ('\nFIM DO PROGRAMA!')
