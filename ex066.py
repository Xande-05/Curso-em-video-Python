n = s = t = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    t += 1
print (f'A soma dos {t} valores digitados foi de {s}.')