def notas(*num, sit):
    soma = 0
    for c in num:
        soma += c
    média = soma / len(num)
    if sit:
        if média > 7:
            sit = 'boa'
        elif média > 5:
            sit = 'regular'
        else:
            sit = 'ruim'
        return (f'Total: {len(num)} notas - Maior: {max(num)} - Menor: {min(num)} - Média: {média:.1f} e a situação da turma é {sit}.')
    else:
        return (f'Total: {len(num)} notas - Maior: {max(num)} - Menor: {min(num)} - Média: {média:.1f}.')

resp = notas(1.3, 5.7, 10, 7.5, sit=True)
print(resp)