#Utilizando dicionários em python: métos de declarar um dicionário

pessoa = {"Nome": "Guilherme", "Idade": 28}

pessoa = dict(nome = "Gabriela", idade = 25)

pessoa["telefone"] = "3333-1234"


#acessando dados do dicionário
pessoa["nome"] = "Ariela" #alterando o valor da variável
#exibindo o valor da variável
print(pessoa["nome"])

#Dicionário Aninhado

contatos = {
    "gabi11-@live.com": {"nome": "gabriela", "idade": 25},
    "gabi12luar@gmail.com": {"nome": "Gabi", "idade": 26}
}

print(contatos["gabi11-@live.com"]["idade"])

#interar dicionários: vai percorrer todos os elementos do dicionário

for contato in contatos:
    print(contato, contatos[contato])