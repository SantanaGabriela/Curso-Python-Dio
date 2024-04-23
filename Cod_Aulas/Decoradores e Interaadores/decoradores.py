def mensagem(nome):
    print('Executanfo nome')
    return f'Oi {nome}'


def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f'Olá tudo bem com você {nome} ?'

def executar(funcao,nome):
    print("Executano executar")
    return funcao(nome)


print(executar(mensagem('Gabriela')))
print(executar(mensagem_longa, "João"))