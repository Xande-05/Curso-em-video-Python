# Dicionário para agrupar participantes por tema
eventos = {}
dados= list()

# Entrada do número de participantes
n = int(input('a: ').strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for c in range (0, n):
    nome = (str(input('b: ')).strip())
    trabalho = (str(input('c: ')).strip())
    eventos = [nome, trabalho]
    if trabalho in eventos:
        eventos[trabalho].append(nome)
    dados.append(eventos.copy())


print (dados)
# Exibe os grupos organizados
'''for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")'''