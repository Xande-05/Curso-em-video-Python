print ('Digite aqui quantos números quiser até decidir parar [S/N]')
desejo = 'S'
contador = soma = maior = menor = 0
while desejo == 'S':
    contador += 1
    numero = int(input('Digite aqui um número: '))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor or menor == 0:
        menor = numero
    desejo = input ('Deseja continuar [S/N]? ').upper().strip()
print ('A média entre todos os valores foi de: {}'.format(soma / contador))
print ('O maior valor digitado foi o {} e o menor valor digitado foi o {}'.format(maior, menor))