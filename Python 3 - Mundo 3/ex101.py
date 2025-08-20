def voto(data):
    from datetime import date
    ano = date.today().year
    idade = ano - nascmento
    if idade < 16:
        situação= 'negado'
    elif idade > 65 or 16 <= idade < 18:
        situação= 'opcional'
    else:
        situação= 'obrigatório'
    return (f'Você tem {idade} anos e seu voto é {situação}!')


nascmento= int(input('Digite seu ano de nascimento: '))
print (voto(nascmento))