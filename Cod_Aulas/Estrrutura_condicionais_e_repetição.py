MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH")




if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

else:
    print("Menor de idade, não pode tirar a CNH")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
    
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas")

else:
    print("Menor de idade, não pode tirar a CNH")