# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':


# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 
    

# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self._saldo = plano

    def verifica_saldo(self):
        if self._saldo <10:
            return  self._saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >=50:
            return self._saldo,  "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self._saldo,  "Seu saldo está razoável. Aproveite o uso moderado do seu plano."



# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)