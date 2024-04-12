quantidade_passos = int(input())

if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    for passo in range(1, quantidade_passos + 1):
        print(f'explorador: {passo} passo{"s" if passo > 1 else ""}')