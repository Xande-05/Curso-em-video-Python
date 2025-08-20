abreparentese = 0
fechaparentese = 0
conta = input('Digite uma expressão matemática: ')
if "(" in conta:
    abreparentese += 1
if ")" in conta:
    fechaparentese += 1
if abreparentese == fechaparentese:
    print ('Sua equação é possível.')
else:
    print('Sua equação não é posivel.')