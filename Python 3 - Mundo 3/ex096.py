def area(base, altura):
    total= base * altura
    print (f'A área do seu terreno de {base}x{altura} é de {total:.1f}M²')


print ('MEDINDO SEU TERRENO')
print ('-'*30)
largura = float(input('Largura em M: '))
comprimento= float(input('Comprimento em M: '))
area(largura, comprimento)