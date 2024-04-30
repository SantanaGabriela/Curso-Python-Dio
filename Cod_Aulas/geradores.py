def meu_gerador(numeros = list[int]):
    for numero in numeros:
        yield numeros * 2 # retorna o valor. tem a mesma função do return


for i in meu_gerador(numeros = [1,2,3]):
    print(i)