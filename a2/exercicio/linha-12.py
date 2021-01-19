def corrigir_telefone(telefone, formatar=True):
    telefone_sem_hifen = telefone.replace('-', '')
    qtd_caracteres = len(telefone_sem_hifen)
    telefone_corrigido = telefone_sem_hifen
    if qtd_caracteres < 8:
        print(f'Telefone possui {qtd_caracteres} dígitos. Vou acrescentar o digito três na frente.')
        caracteres_faltantes = 8 - qtd_caracteres
        telefone_corrigido = caracteres_faltantes * '3' + telefone_sem_hifen
    if formatar:
        telefone_corrigido = telefone_corrigido[0:4] + '-' + telefone_corrigido[4:8]
    return telefone_corrigido
if __name__ == '__main__':
    print('Valida e corrige número de telefone:')
    print('Telefone:')
    telefone = str(input())
    print('Telefone corrigido sem formatação:', corrigir_telefone(telefone, formatar=False))
    print('Telefone corrigido com formatação:', corrigir_telefone(telefone))