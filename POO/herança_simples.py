class veiculo:
    def __init__(self, cor, placa,numero_rodas):
        self.cor= cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o Motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(veiculo):
    pass

class Carro(veiculo):
    pass

class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
       super().__init__(cor, placa, numero_rodas)
       self.carregado = carregado
   
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado  else 'Não'} estou carregado")




moto = Motocicleta("vermelha", "abc-123", 2)
#print(moto)
#moto.ligar_motor()

carro = Carro("Branco", "bvc-456", 4)
#carro.ligar_motor()

caminhao = Caminhao("Roxo", "PGF-567", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
print(carro)
print(moto)

