class Pessoa:
    def __init__(self, nome=None, idade=None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano,mes,idade,nome):
        idade = 2024- ano
        return cls(nome,idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("Gabriela", 25)
#print(p.nome,p.idade)

p2 = Pessoa().criar_de_data_nascimento(1998,6,23,"Gabriela")
print(p2.nome,p2.idade)

print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(28))