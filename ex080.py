tabela = []
for c in range (0, 5):
    lista = int(input(f'Digite aqui o {c+1}° valor: '))
    if c == 0 or lista > tabela[-1]:
        print ('Valor adicionado no final da lista...')
        tabela.append(lista)
    else:
        for c in range(0, len(tabela)):
            if lista <= tabela[c]:
                tabela.insert(c, lista)
                print (f'Valor adicionado na osição {c} da lista...')
                break
            c += 1
print (tabela)