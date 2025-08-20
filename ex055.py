mai = 0
men = 0
for c in range(0, 5):
    p = float (input('Digite um peso em Kg: '))
    if p > mai:
        mai = p
    elif p < men or men == 0:
        men = p
print ('O maior peso foi de {}Kg'.format(mai))
print ('O menor peso foi de {}Kg'.format(men))