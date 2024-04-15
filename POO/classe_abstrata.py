from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    def desligar(self):
        pass


class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando Tv")
        print("Ligada")

    def desligar(self):
        print("Desligando TV")
        print("Desligado")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligado")

    def desligar(self):
        print("Desligado")

    

controle = ControleTv()

controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
