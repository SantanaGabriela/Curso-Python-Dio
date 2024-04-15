class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    
    @property
    def nome (self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


   # def get_nome(self):
        #return self._nome
    
   # def get_idade(self):
        #return 2024 - self._ano.nascimento

pessoa = Pessoa("Gabi", 1998)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
#print(f"Nome: {pessoa.get_nome} \tIdade: {pessoa.get_idade}")