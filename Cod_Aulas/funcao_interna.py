def principal():
    print('Executando a função principal')

    def funcao_interna():
        print("Executando função interna")

    def funcao_2():
        print("executando a função 2")

    funcao_interna()
    funcao_2()

principal()