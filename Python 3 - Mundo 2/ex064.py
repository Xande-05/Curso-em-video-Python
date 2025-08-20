print ('Vamos fazer uma soma com quantos números quiser, para parar, basta digitar "999"')
num = soma = quantidade = 0
num = int(input('Digite aqui um número: '))
while num != 999:
    soma += num
    quantidade += 1
    num = int(input ('Digite aqui um número: '))
print ('Foram digitados {} valores e a soma entre eles foi de: {}'.format(quantidade, soma))