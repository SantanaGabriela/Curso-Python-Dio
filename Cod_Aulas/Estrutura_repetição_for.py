texto = input("informe um texto")
VOGAIS = "AEIOU"
#exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


#range(start, sotp, step) exemplo com range
for numero in range (0,51,10):
    print(numero, end=" ")