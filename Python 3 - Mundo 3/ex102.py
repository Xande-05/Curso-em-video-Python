def fatorial(número, show=True):
    """
    :param número:
    :param show:
    :return:
    """
    f = 1
    for c in range(número, 0, -1):
        f *= c
        if show:
            if c == 1:
                print (f' {c} =', end='')
            else:
                print (f' {c} x', end='')
    return (f' {f}')


n= (int(input('Digite um númeropara saber sua fatorção: ')))
opção= (str(input('Gostaria de ver a equação? [S/N]:'))).upper()
if opção not in 'SsNn':
    while opção not in 'SsNn':
       opção= (str(input('Resposta inválida, por favor digite "S" ou "N": '))).upper()
if opção == 'S':
    print (fatorial(n))
else:
    print (fatorial(n, False))