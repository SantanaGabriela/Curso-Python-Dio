#Listas: É uma sequencia que pode armazenar qualqueer tipo de objeto/itens.
#Criando Listas - Tipos de construtores#

#list(1,2,3,4)
#Notas = [1,2,3]
#print(list)
#print(Notas)

#lista vazia
Frutas =[]
print(Frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferraro", "f8", 420000, 2020, 2900,"São Paulo", True]
print(carro)


#Lista aninhadas: é quando existe uma lista dentro de outra lista.

matriz = [
    [1,"a",2],
    ["b,",3,4],
    [6,5,"c"],
]
# [linha][coluna]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#Fateamento

#acessar o elemento da lista dando um inicio ou um fim, podendo ter também um step que vai indicar de quanto em quanto vai pular a casa.

lista= ["p","u","t","a"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]#[inicio:fim:step] = anda de 2 em 2 como definido no step
lista[::] #= retorna a sequencia padrão, uma cópia da lista.
lista[::-1] #=  espelha/inverte uma sequência. 

#Iterar Lista = forma mais comum de percorrer uma lista é utilizando o comando for

carros = ["gol", "celta", "palio"]

for carro in carros:
	print(carro)
      
#funcao enumerate: vai enumerar os elementos da lista utilizando a função for
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f" {indice}: {carro}")


#compreenção dee lista

numeros = [1,30,21,2,9,65,34]
pares= []

for numero in numeros:
      if numero % 2 == 0:
            pares.append(numero)


