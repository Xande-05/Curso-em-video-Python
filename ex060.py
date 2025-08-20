n = int (input ('Escolha um número para sabermos seu fatorial: '))
contador = n - 1
while contador != 0:
    fatorial = n * contador
    n = fatorial
    contador -= 1
print (fatorial)