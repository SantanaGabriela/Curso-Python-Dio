def exibir_mensagem():
	print("Olá, Mundo")

def exibir_mensagem_1(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_2(nome = "Gabriela"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem_1(nome="Gabriela")
exibir_mensagem_2()
exibir_mensagem()

#retornando valores

def calcular_total(numeros):
     return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
     antecessor = numero - 1
     sucessor = numero + 1

     return antecessor, sucessor


def func_3():
     print("Olá")

func_3()
print(calcular_total([10,20,30]))
print(retorna_antecessor_e_sucessor(10))

#Argumento nomeado

def salvar_carro(marca,modelo, ano, placa):
  print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat", "palio", 1999,"ABC-123")#menos seguro, pois não respeita a ordem. 
salvar_carro(marca = "fiat", modelo=" palio", ano =1990, placa= "ABC-123")#atribuindo valores as variaveis
salvar_carro(**{"marca":"fiat", "modelo":"palio", "ano": 1999, "placa":"ABC-123"})#atribuindo valores usando dicionário