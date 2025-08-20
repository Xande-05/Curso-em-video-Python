def linha(msg):
    letras = len(msg) + 4
    print('-' * letras)
    print(' ', msg)
    print('-' * letras)


palavra = str(input('Qual frase ou palavra que você deseja: ')).strip()
linha(palavra)