times = 'Fla', 'Flu', 'Bot', 'Vas', 'SãoP', 'Pal', 'San', 'Chapeco', 'Esport', 'Cor', 'Boca', 'Inter', 'Cruz', 'AtlM', 'JoinV', 'AtlP'
print (times)
print (f'A - Os 5 primeiros colocados do campeonato são: {times[:5]}')
print (f'B - Os 4 últimos times do campeonato são: {times[-4:]}')
print (f'C - Em ordem alabética: {sorted(times)}')
print (f'D - O time Chapecoense na tabela está na posição {times.index("Chapeco")+1}')
