class UsuariaTelefone:

    def __init__(self, nome , numero , plano) -> None:
        self.nome = nome
        self.numero = numero
        self.plano = plano

      
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

@property
def nome(self):
    return self.nome

property
def numero(self):
    return self._numero

property
def plano(self):
    return self._plano


# Entrada:
nome = input()  
numero = input()  
plano = input()  

usuario = UsuariaTelefone(nome,numero,plano)

print(usuario)