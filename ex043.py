p= float (input ('Digite aqui seu peso em Kg: '))
a= float (input ('Digite aqui sua altura em metros: '))
imc= p / a**2
if imc < 18.5:
    print ('Abaixo do peso')
if 18.5 <= imc < 25:
    print ('Peso ideal')
if 25 <= imc < 30:
    print ('Sobrepeso')
if 30 <= imc < 40:
    print ('Obesidade')
if imc >= 40:
    print ('Obesidade mórbida')